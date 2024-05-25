<template>
  <div class="device-list">
    <div class="row q-pa-lg">
      <div class="col-12">
        <p class="device-list__title text-white text-left text-h5 q-pb-lg q-px-md">Устройства</p>
      </div>
      <div
        class="col-12 text-white text-h6 q-px-md"
        v-if="!userDevices || userDevices.length === 0"
      >
        <p>Доступные устройства не найдены</p>
      </div>
      <div
        class="device-list__devices col-6 q-px-md q-mt-md"
        v-else
        v-for="userDevice in userDevices"
        :key="userDevice?.id"
      >
        <div class="control-buttons column">
          <!-- <q-btn
            class="edit-btn"
            round
            color="yellow-14"
            icon="edit"
            size="sm"
            @click="console.log('click')"
          /> -->
          <q-btn
            class="remove-btn"
            round
            color="red"
            icon="delete"
            size="sm"
            @click="deleteDevice(userDevice.id)"
          />
        </div>
        <q-card class="column items-center">
          <q-card-section class="q-py-sm">
            <q-avatar size="40px">
              <img :src="GeneralDevice">
            </q-avatar>
          </q-card-section>
          <q-card-section class="row items-center q-pt-sm">
            <p class="text-body1">{{ userDevice.name }}</p>
          </q-card-section>
        </q-card>
      </div>
    </div>
    <div class="device-list__tooltip">Добавить устройство</div>
    <q-btn
      class="symptom-list__btn"
      color="white"
      size="lg"
      round
      @click="showDialog = true"
    >
      <q-icon
        name="add"
        color="deep-purple-9"
        size="xl"
      />
    </q-btn>
    <q-dialog
      class="device-dialog"
      v-model="showDialog"
      position="bottom"
      :persistent="false"
    >
      <q-list class="device-dialog__list">
        <q-item class="title text-h5 text-white justify-center">Добавить устройство</q-item>
        <q-item
          class="device q-px-xl"
          v-for="device in listDevicesWithoutUserDevices"
          :key="device.id"
        >
          <q-item-section class="row q-px-xl">
            <q-card class="row items-center justify-between q-pa-sm">
              <q-card-section class="q-py-none q-px-sm text-h6">
                <q-avatar>
                  <img :src="GeneralDevice">
                </q-avatar>
                {{ device.name }}
              </q-card-section>
              <q-card-actions>
                <q-btn
                  round
                  color="green"
                  icon="add"
                  size="sm"
                  @click="addDevice(device.id)"
                />
              </q-card-actions>
            </q-card>
          </q-item-section>
        </q-item>
      </q-list>
    </q-dialog>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'
import { useDevice } from 'src/composables/useDevice'
import { Device } from 'src/models'
import { Notify } from 'quasar'
import GeneralDevice from 'images/general_device.svg'

const { getDeviceList, getUserDevice, asignUserDevice, removeUserDevice } = useDevice()

const userDevices = ref<Device[]>()
const listDevices = ref<Device[]>()

const showDialog = ref<boolean>(false)
const user_id = ref<number>()

const deleteDevice = async (device_id: number | string | undefined) => {
  await removeUserDevice(user_id.value, device_id)
    .then(() => {
      Notify.create({
        color: 'positive',
        message: 'Устройство успешно удалено!',
        position: 'top'
      })
      if (userDevices.value) {
        userDevices.value = userDevices.value.filter(device => device.id !== device_id);
      }
    })
    .catch((error) => {
      Notify.create({
        color: 'negative',
        message: 'Произошла ошибка, попробуйте позже!',
        position: 'top'
      })
      console.error(error)
    })
}

const addDevice = async (device_id: number | string | undefined) => {
  const device_data = {
    "device_id": [
      device_id
    ]
  }
  await asignUserDevice(user_id.value, device_data)
    .then(() => {
      Notify.create({
        color: 'positive',
        message: 'Устройство успешно добавлено!',
        position: 'top'
      })
      if (userDevices.value && listDevices.value) {
        const newDevice = listDevices.value.find(device => device.id === device_id);
        if (newDevice) {
          userDevices.value.push(newDevice);
        }
      }
    })
    .catch((error) => {
      Notify.create({
        color: 'negative',
        message: 'Произошла ошибка, попробуйте позже!',
        position: 'top'
      })
      console.error(error)
    })
};

const listDevicesWithoutUserDevices = computed(() => {
  if (listDevices.value && userDevices.value) {
    return listDevices.value.filter(device => !userDevices.value.some(userDevice => userDevice.id === device.id));
  }
  return [];
});

onMounted(async () => {
  user_id.value = Number(localStorage.getItem('userId'))
  try {
    const responseUser = await getUserDevice(user_id.value)
    const responseList = await getDeviceList()
    userDevices.value = responseUser.data
    listDevices.value = responseList.data
  } catch (error) {
    console.error(error)
  }
})
</script>

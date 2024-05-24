<template>
  <div
    class="device-list"
    style="width: 100%;"
  >
    <div class="row q-pa-lg">
      <div class="col-12">
        <p class="text-white text-left text-h5 q-pb-lg q-px-md">Устройства</p>
      </div>
      <div
        class="col-12 text-white text-h6"
        v-if="!userDevices || userDevices.length === 0"
      >
        <p>Доступные устройства не найдены</p>
      </div>
      <div
        class="col-6 q-px-md q-mt-md"
        v-else
        v-for="userDevice in userDevices"
        :key="userDevice?.id"
      >
        <q-card class="column items-center">
          <q-card-section class="q-py-sm">
            <q-avatar size="40px">
              <img :src="GeneralDevice">
            </q-avatar>
          </q-card-section>
          <q-card-section class="row items-center">
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
      <q-list style="border-radius: 50px 50px 0 0; background-color: rgba(73, 42, 79, 15%); background-color: #D6D0E8;">
        <q-item class="device-dialog__title text-h5 text-white justify-center">Добавить устройство</q-item>
        <q-item
          class="q-px-xl"
          style="padding-top: 0; width: auto;"
          v-for="device in listDevices"
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
import { ref, onMounted } from 'vue'
import { useDevice } from 'src/composables/useDevice'
import { Device } from 'src/models'
import { Notify } from 'quasar'
import GeneralDevice from 'images/general_device.svg'

const { getDeviceList, getUserDevice, asignUserDevice } = useDevice()

const userDevices = ref<Device[]>()
const listDevices = ref<Device[]>()

const showDialog = ref<boolean>(false)
const user_id = ref<number>()

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
    })
    .catch((error) => {
      alert(error)
    })
};

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

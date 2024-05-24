<template>
  <div
    class="device-list"
    style="width: 100%;"
  >
    <div class="row q-pa-lg">
      <div class="col-12">
        <p class="text-white text-left text-h5 q-pb-lg">Устройства</p>
      </div>
      <div
        class="col-12 text-white text-h6"
        v-if="!userDevices || userDevices.length === 0"
      >
        <p>Доступные устройства не найдены</p>
      </div>
      <div
        class="col-6"
        v-else
        v-for="userDevice in userDevices"
        :key="userDevice?.id"
      >
        <q-card class="row">
          <q-card-section class="q-py-sm">
            <q-avatar>
              <img :src="GeneralDevice">
            </q-avatar>
          </q-card-section>
          <q-card-section class="row items-center">
            <p class="text-h6">{{ userDevice.name }}</p>
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
          style="padding-top: 0;"
          v-for="device in listDevices"
          :key="device.id"
          clickable
          v-ripple
        >
          <q-item-section class="row q-px-xl items-center">
            <q-card
              class="row justify-between q-px-sm"
              style="width: 12rem;"
            >
              <q-item-label>
                <q-avatar>
                  <img :src="GeneralDevice">
                </q-avatar>
              </q-item-label>
              <q-item-label class="row justofy-center items-center text-h6">{{ device.name }}</q-item-label>
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
import GeneralDevice from 'images/general_device.svg'

const { getDeviceList, getUserDevice } = useDevice()

const userDevices = ref<Device[]>()
const listDevices = ref<Device[]>()

const showDialog = ref<boolean>(false)

const asignDevice = () => {
  // реализация добавления симптома
}

onMounted(async () => {
  const user_id = Number(localStorage.getItem('userId'))
  try {
    const responseUser = await getUserDevice(user_id)
    const responseList = await getDeviceList()
    userDevices.value = responseUser.data
    listDevices.value = responseList.data
  } catch (error) {
    console.error(error)
  }
})
</script>

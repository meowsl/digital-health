<template>
  <q-layout
    view="hhh lpR fFf"
    v-if="mediaIsPhone"
  >
    <q-header class="header">
      <q-toolbar class="header__toolbar row justify-between q-pa-lg">
        <q-btn
          flat
          round
          dense
          icon="menu"
          @click="drawer = !drawer"
          class="q-mr-sm"
        />
        <q-avatar size="65px">
          <img :src="Placeholder">
        </q-avatar>
      </q-toolbar>

    </q-header>
    <q-drawer
      class="q-pa-lg text-white"
      v-model="drawer"
      show-if-above
      style="background-color: #D9D3EB;"
    >
      <q-card
        flat
        class="menu__card"
      >
        <q-card-section class="row items-center justify-center">
          <q-avatar size="60px">
            <img :src="Placeholder">
          </q-avatar>
          <p class="text-h5 q-ml-sm q-mb-none">{{ firstname }} {{ lastname?.substring(0, 2) }}.</p>
        </q-card-section>
      </q-card>
      <q-separator
        dark
        size="2px"
        spaced="12px"
      />
      <q-list class="col justify-center items-center text-center text-h5">
        <q-item
          class="menu__nav-item"
          clickable
          v-ripple
          to="/"
        >
          <q-avatar
            square
            size="40px"
          >
            <img :src="NotifyIcon">
          </q-avatar>
          <q-item-section>Уведомления</q-item-section>
        </q-item>
        <q-item
          class="menu__nav-item"
          clickable
          v-ripple
          to="/measurements"
        >
          <q-avatar
            square
            size="40px"
          >
            <img :src="MeasureIcon">
          </q-avatar>
          <q-item-section>Показатели</q-item-section>
        </q-item>
        <q-item
          class="menu__nav-item"
          clickable
          v-ripple
          to="/symptoms"
        >
          <q-avatar
            square
            size="40px"
          >
            <img :src="SymptomIcon">
          </q-avatar>
          <q-item-section>Симптомы</q-item-section>
        </q-item>
        <q-item
          class="menu__nav-item"
          clickable
          v-ripple
          to="/activity"
        >
          <q-avatar
            square
            size="40px"
          >
            <img :src="ActivityIcon">
          </q-avatar>
          <q-item-section>Активность</q-item-section>
        </q-item>
        <q-item
          class="menu__nav-item"
          clickable
          v-ripple
          to="/devices"
        >
          <q-avatar
            square
            size="40px"
          >
            <img :src="DevicesIcon">
          </q-avatar>
          <q-item-section>Устройства</q-item-section>
        </q-item>
        <q-item
          class="menu__nav-item"
          clickable
          v-ripple
          to="/family"
        >
          <q-avatar
            square
            size="40px"
          >
            <img :src="FamilyIcon">
          </q-avatar>
          <q-item-section>Семья</q-item-section>
        </q-item>
        <q-item
          class="menu__nav-item"
          clickable
          v-ripple
          to="/documents"
        >
          <q-avatar
            square
            size="40px"
          >
            <img :src="DocsIcon">
          </q-avatar>
          <q-item-section>Документы</q-item-section>
        </q-item>
        <q-item
          class="menu__nav-item"
          clickable
          v-ripple
          to="/settings"
        >
          <q-avatar
            square
            size="40px"
          >
            <img :src="SettingsIcon">
          </q-avatar>
          <q-item-section>Настройки</q-item-section>
        </q-item>
      </q-list>
    </q-drawer>
    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
  <q-layout
    view="lHh Lpr lFf"
    v-else
  >
    <q-page-container>
      <NoMobile />
    </q-page-container>
  </q-layout>
</template>

<script setup lang='ts'>
import { ref, onMounted } from 'vue'
import { useAuthStore } from 'src/stores/auth'
import { Notify } from 'quasar'
import { useUser } from 'src/composables/useAuth'
import Placeholder from 'images/avatar_placeholder.png'
import NotifyIcon from 'images/menu/notifications.svg'
import MeasureIcon from 'images/menu/measurements.svg'
import SymptomIcon from 'images/menu/symptoms.svg'
import ActivityIcon from 'images/menu/activity.svg'
import DevicesIcon from 'images/menu/devices.svg'
import FamilyIcon from 'images/menu/family.svg'
import DocsIcon from 'images/menu/documents.svg'
import SettingsIcon from 'images/menu/settings.svg'
import NoMobile from 'src/components/NoMobile.vue'


const authStore = useAuthStore()
const { getUserInfo } = useUser()

const mediaIsPhone = ref<boolean>(false)
const drawer = ref(false)

const firstname = ref<string>()
const lastname = ref<string>()

onMounted(async () => {
  const mediaQuery = window.matchMedia('(max-width: 480px)');
  mediaIsPhone.value = mediaQuery.matches;
  mediaQuery.addListener((event) => {
    mediaIsPhone.value = event.matches
  });
  const userIdFromStorage = localStorage.getItem('userId')
  const token = localStorage.getItem('token')
  if (userIdFromStorage !== null && token !== null) {
    const dataUser = await getUserInfo(Number(userIdFromStorage))
    authStore.user = {
      id: dataUser.data.id,
      firstName: dataUser.data.firstName,
      lastName: dataUser.data.lastName,
      username: dataUser.data.username,
      email: dataUser.data.email
    }
  } else {
    authStore.userLogout()
    Notify.create({
      color: 'negative',
      message: 'Пожалуйста, авторизуйтесь снова!',
      position: 'top'
    })
  }

})
</script>
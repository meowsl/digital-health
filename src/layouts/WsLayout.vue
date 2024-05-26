<template>
  <q-layout view="hhh lpR fFf">
    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script setup lang='ts'>
import { ref, onMounted } from 'vue';
import { useAuthStore } from 'src/stores/auth'
import { Notify } from 'quasar';
import { useUser } from 'src/composables/useAuth'

const authStore = useAuthStore()
const { getUserInfo } = useUser()


const firstName = ref<string>()
const lastName = ref<string>()

onMounted(async () => {
  const userIdFromStorage = localStorage.getItem('userId')
  const token = localStorage.getItem('token')
  if (userIdFromStorage == null || token == null) {
    authStore.userLogout()
    Notify.create({
      color: 'negative',
      message: 'Пожалуйста, авторизуйтесь снова!',
      position: 'top'
    })
  } else {
    const dataUser = await getUserInfo(Number(userIdFromStorage))
    authStore.setUser({
      id: dataUser.data.id,
      firstName: dataUser.data.firstname,
      lastName: dataUser.data.lastname,
      username: dataUser.data.username,
      email: dataUser.data.email
    })
    firstName.value = dataUser.data.firstname
    lastName.value = dataUser.data.lastname
  }
})

</script>
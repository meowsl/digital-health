<template>
  <q-form
    class="auth-form column text-white justify-center q-py-lg q-px-xl"
    @submit.prevent="submitLogin()"
    v-if="loginForm"
  >
    <p class="auth-form__title text-center q-pb-lg text-h5">Авторизация</p>
    <q-input
      class="auth-form__input q-pb-lg"
      v-model="username"
      standout
      type="text"
      placeholder="Логин или e-mail"
      lazy-rules
      :rules="[val => !!val || 'Обязательное поле']"
    />
    <q-input
      class="auth-form__input q-pb-lg"
      v-model="password"
      standout
      type="password"
      placeholder="Пароль"
      lazy-rules
      :rules="[val => !!val || 'Обязательное поле']"
    />
    <q-btn
      class="auth-form__button-submit"
      no-caps
      filled
      rounded
      :loading="loadingBtn"
      label="Войти"
      type="submit"
    />
    <q-btn
      class="auth-form__button-registration"
      no-caps
      unelevated
      flat
      rounded
      label="Нет аккаунта?"
      @click="loginForm = false"
    />

  </q-form>
  <q-form
    class="auth-form column text-white justify-center q-py-lg q-px-xl"
    @submit.prevent="submitRegistration()"
    v-else
  >
    <p class="auth-form__title text-center q-pb-lg text-h5">Регистрация</p>
    <q-input
      class="auth-form__input q-pb-lg"
      v-model="firstname"
      standout
      type="text"
      placeholder="Имя"
      lazy-rules
      :rules="[val => !!val || 'Обязательное поле']"
    />
    <q-input
      class="auth-form__input q-pb-lg"
      v-model="lastname"
      standout
      type="text"
      placeholder="Фамилия"
      lazy-rules
      :rules="[val => !!val || 'Обязательное поле']"
    />
    <q-input
      class="auth-form__input q-pb-lg"
      v-model="username"
      standout
      type="text"
      placeholder="Имя пользователя"
      lazy-rules
      :rules="[val => !!val || 'Обязательное поле']"
    />
    <q-input
      class="auth-form__input q-pb-lg"
      v-model="email"
      standout
      type="text"
      placeholder="E-mail"
      lazy-rules
      :rules="[val => !!val || 'Обязательное поле']"
    />
    <q-input
      class="auth-form__input q-pb-lg"
      v-model="password"
      standout
      type="password"
      placeholder="Пароль"
      lazy-rules
      :rules="[val => !!val || 'Обязательное поле']"
    />
    <q-btn
      class="auth-form__button-submit"
      no-caps
      filled
      rounded
      :loading="loadingBtn"
      label="Подтвердить"
      type="submit"
    />
    <q-btn
      class="auth-form__button-registration"
      no-caps
      unelevated
      flat
      rounded
      label="Уже есть аккаунт?"
      @click="loginForm = true"
    />
  </q-form>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useAuthStore } from 'src/stores/auth'
import { Notify } from 'quasar'

const authStore = useAuthStore()

const username = ref<string>('')
const password = ref<string>('')
const email = ref<string>('')
const firstname = ref<string>('')
const lastname = ref<string>('')

const loginForm = ref<boolean>(true)
const loadingBtn = ref<boolean>(false)

const submitLogin = async () => {
  loadingBtn.value = true
  try {
    await authStore.userLogin(username.value, password.value)
  }
  catch (error) {
    console.log(error)
  }
  finally {
    loadingBtn.value = false
  }
}

const submitRegistration = async () => {
  loadingBtn.value = true
  const data = {
    "firstname": firstname.value,
    "lastname": lastname.value,
    "email": email.value,
    "username": username.value,
    "password": password.value,
    "role": "user"
  }
  try {
    await authStore.userRegistration(data)
      .then(e => {
        Notify.create({
          color: 'positive',
          message: 'Успешная регистрация!',
          position: 'top'
        })
        loginForm.value = true
      })
      .catch(e => {
        console.log(e)
        Notify.create({
          color: 'negative',
          message: 'Ошибка регистрации!',
          position: 'top'
        })
      })
  }
  catch (error) {
    console.log(error)
  }
  finally {
    loadingBtn.value = false
  }
}
</script>
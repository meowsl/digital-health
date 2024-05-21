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
      type="text"
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
      type="text"
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

const username = ref<string>()
const password = ref<string>()
const email = ref<string>()

const loginForm = ref<boolean>(true)
const loadingBtn = ref<boolean>(false)

const submitLogin = async () => {
  loadingBtn.value = true
  console.log('placehold')
}

const submitRegistration = async () => {
  loadingBtn.value = true
  console.log('placehold')
}
</script>
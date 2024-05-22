import { boot } from 'quasar/wrappers'
import axios, { AxiosInstance, AxiosResponse, AxiosError } from 'axios'
import { useAuthStore } from 'src/stores/auth'
import { Notify } from 'quasar'
declare module '@vue/runtime-core' {
  interface ComponentCustomProperties {
    $axios: AxiosInstance
    $api: AxiosInstance
  }
}

const api = axios.create({
  baseURL: process.env.DEV ? 'http://localhost:8000/' : '/',
  withCredentials: true,
  headers: { 'Content-Type': 'application/json' },
})

export default boot(({ app }) => {
  const authStore = useAuthStore()
  app.config.globalProperties.$axios = axios
  app.config.globalProperties.$api = api
  api.interceptors.response.use(
    (response: AxiosResponse) => {
      return response
    },
    (error: AxiosError) => {
      if (error.response?.status === 401) {
        Notify.create({
          color: 'negative',
          message: 'Пожалуйста, авторизуйтесь снова!',
          position: 'top'
        })
        authStore.userLogout()
        return error.response?.status
      } else if (error.response?.status === 400) {
        Notify.create({
          color: 'negative',
          message: 'Проверьте введенные данные и попробуйте снова!',
          position: 'top'
        })
      }
      return Promise.reject(error)
    },
  )
})


export { api }

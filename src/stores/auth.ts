import { defineStore } from 'pinia'
import { api } from 'src/boot/axios'
import { AuthState } from 'src/models/auth'

export const useAuthStore = defineStore('authStore', {
  state: (): AuthState => ({
    user: {
      id: undefined,
      firstName: undefined,
      lastName: undefined,
      username: undefined,
      email: undefined,
    },
  }),
  actions: {
    setUser(user: any) {
      this.user = user
    },
    async userLogin(username: string, password: string) {
      await api
        .post('/user/login', { username, password })
        .then(e => {
          console.log(e.data.data)
          const token = e.data.data.access
          localStorage.setItem('token', token)
          this.router.push({ name: 'WsPage' })
          if (this.user && e.data.data.user_id) {
            localStorage.setItem('userId', e.data.data.user_id)
          }
        })
        .catch(e => {
          if (e.status === 401) {
            console.log(e.status)
            alert('Invalid username or password')
          }
        })
    }
    ,
    async userLogout() {
      localStorage.removeItem('token')
      localStorage.removeItem('user_id')
      this.router.push({ name: 'AuthPage' })
    },
    clear() {
      this.user = null
    },
    async userRegistration(data: object) {
      await api
        .post('/user/register', data)
    }
  }
})
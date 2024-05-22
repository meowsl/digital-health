import { defineStore } from 'pinia'
import { api } from 'src/boot/axios'
import { AuthState } from 'src/models/auth'

export const useAuthStore = defineStore('authStore', {
  state: (): AuthState => ({
    user: {
      id: undefined,
      firstName: undefined,
      lastName: undefined
    },
  }),
  actions: {
    async userLogin(username: string, password: string) {
      await api
        .post('/user/login', { username, password })
        .then(e => {
          const token = e.data.data.access
          localStorage.setItem('token', token)
          this.router.push({ name: 'IndexPage' })
          if (this.user && e.data.data.firstname && e.data.data.lastname) {
            localStorage.setItem('firstname', e.data.data.firstname)
            localStorage.setItem('lastname', e.data.data.lastname)
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
      localStorage.removeItem('firstname')
      localStorage.removeItem('lastname')
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
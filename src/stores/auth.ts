import { defineStore} from "pinia"
import { api } from "src/boot/axios"
import { AuthState } from "src/models/auth"

export const useAuthStore = defineStore('authStore', {
  state: (): AuthState => ({
    user: {
      id: undefined,
      firstName: undefined,
      lastName: undefined
    },
  }),
  actions: {
    async userLogin(username: string, password: string){
      await api
        .post('/user/login', {username, password})
        .then(e => {
          const token = e.data.data.access
          localStorage.setItem('token', token)
          this.router.push({name: 'IndexPage'})
        })
        .catch(e => {
          if (e.response.status === 401){
            alert('Invalid username or password')
          }
        })
    },
    async userLogout(){
      localStorage.removeItem('token')
    },
    clear(){
      this.user = null
    }
  }
})
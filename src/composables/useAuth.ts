import { User } from 'src/models/auth'
import { api } from 'src/boot/axios'

export const getAuthToken = () => {
  if (localStorage.getItem('token')) {
    return `Bearer ${localStorage.getItem('token')}`
  }
}

export function useUser() {

  const getUserInfo = (id: number) => {
    return api.get(`user/${id}`)
  }

  return {
    getUserInfo
  }
}
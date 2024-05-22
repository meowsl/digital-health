import { Device } from 'src/models'
import { api } from 'src/boot/axios'
import { getAuthToken } from './useAuth'

/* TODO */
export function useDevice() {

  const getDeviceList = () => {
    return api.get<Device[]>('devices')
  }

  return {
    getDeviceList
  }
}
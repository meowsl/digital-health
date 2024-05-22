import { Device } from 'src/models'
import { api } from 'src/boot/axios'
import { getAuthToken } from './useAuth'

/* TODO */
export function useDevice() {

  const getDeviceList = () => {
    return api.get<Device[]>('devices')
  }

  const getDevice = (id: number) => {
    return api.get<Device>(`devices/${id}`)
  }


  return {
    getDeviceList,
    getDevice,
  }
}
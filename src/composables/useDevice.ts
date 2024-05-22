import { Device } from 'src/models'
import { api } from 'src/boot/axios'
import { getAuthToken } from './useAuth'

/* TODO */
export function useDevice() {

  const getDeviceList = () => {
    return api.get<Device[]>('devices')
  }

  const getDevice = (device_id: number) => {
    return api.get<Device>(`devices/${device_id}`)
  }

  const getUserDeviceList = (user_id: number) =>{
    return api.get(`devices/user/${user_id}`)
  }

  const asignUserDevice = (user_id: number, device_data: object) =>{
    return api.post(`devices/user/${user_id}`, device_data)
  }

  return {
    getDeviceList,
    getDevice,
    getUserDeviceList,
    asignUserDevice
  }
}
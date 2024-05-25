import { Device } from 'src/models'
import { api } from 'src/boot/axios'
import { getAuthToken } from './useAuth'

export function useDevice() {

  const getDeviceList = () => {
    return api.get<Device[]>('devices')
  }

  const getDevice = (device_id: number) => {
    return api.get<Device>(`devices/${device_id}`)
  }

  const getUserDevice = (user_id: number) => {
    return api.get(`devices/user/${user_id}`)
  }

  const asignUserDevice = (user_id: number | undefined, device_data: object) => {
    return api.post(`devices/user/${user_id}`, device_data)
  }

  const removeUserDevice = (user_id: number | undefined, device_id: number | string | undefined) => {
    return api.delete(`devices/user/${user_id}/${device_id}`)
  }

  return {
    getDeviceList,
    getDevice,
    asignUserDevice,
    getUserDevice,
    removeUserDevice
  }
}
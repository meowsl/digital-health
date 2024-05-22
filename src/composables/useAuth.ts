export const getAuthToken = () => {
  if (localStorage.getItem('token')) {
    return `Bearer ${localStorage.getItem('token')}`
  }
}
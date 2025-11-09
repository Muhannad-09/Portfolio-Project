import axios from 'axios'

const API = axios.create({
  baseURL: 'http://127.0.0.1:5000/api/v1/auth'
})

export const loginUser = async (data) => {
  const res = await API.post('/login', data)
  alert('Logged in successfully!')
  return res.data
}

export const registerUser = async (data) => {
  const res = await API.post('/register', data)
  alert('Account created successfully!')
  return res.data
}

import axios from 'axios'

const API = axios.create({
  baseURL: 'http://127.0.0.1:5000/api/v1'
})

export const getBooks = async (query) => {
  const res = await API.get(`/books?search=${query}`)
  return res.data
}

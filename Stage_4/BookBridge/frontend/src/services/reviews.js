import axios from 'axios'

// Base API for reviews
const API = axios.create({
  baseURL: 'http://127.0.0.1:5000/api/v1/reviews'
})

// Fetch all reviews for a book
export const getReviews = async (bookId) => {
  const res = await API.get(`/book/${bookId}`)
  return res.data
}

// Add a new review (requires JWT token)
export const addReview = async (bookId, data, token) => {
  const res = await API.post(`/book/${bookId}`, data, {
    headers: { Authorization: `Bearer ${token}` }
  })
  return res.data
}

// Delete a review (only author or admin)
export const deleteReview = async (reviewId, token) => {
  const res = await API.delete(`/${reviewId}`, {
    headers: { Authorization: `Bearer ${token}` }
  })
  return res.data
}


import React from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Navbar from './components/Navbar'
import BookCard from './components/BookCard'
import FavoriteList from './components/FavoriteList'
import Login from './pages/Login'
import Register from './pages/Register'
import SearchBooks from './pages/SearchBooks'
import Favorites from './pages/Favorites'

function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<SearchBooks />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/favorites" element={<Favorites />} />
      </Routes>
    </Router>
  )
}

export default App

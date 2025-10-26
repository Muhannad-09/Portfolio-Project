import React from 'react'
import { Routes, Route } from 'react-router-dom'
import Navbar from './components/Navbar'
import Login from './pages/Login'
import Register from './pages/Register'
import SearchBooks from './pages/SearchBooks'
import Favorites from './pages/Favorites'

const App = () => {
  return (
    <div>
      <Navbar />
      <Routes>
        <Route path="/" element={<SearchBooks />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/favorites" element={<Favorites />} />
      </Routes>
    </div>
  )
}

export default App

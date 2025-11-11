import React, { useEffect, useState } from 'react'
import FavoriteList from '../components/FavoriteList'

const Favorites = () => {
  const [favorites, setFavorites] = useState([])

  useEffect(() => {
    const stored = JSON.parse(localStorage.getItem('favorites')) || []
    setFavorites(stored)
  }, [])

  return (
    <div className="favorites-page">
      <h2>Your Favorite Books</h2>
      <FavoriteList favorites={favorites} />
    </div>
  )
}

export default Favorites

import React from 'react'
import BookCard from './BookCard'

const FavoriteList = ({ favorites }) => (
  <div className="favorite-list">
    {favorites.map((book, i) => <BookCard key={i} book={book} />)}
  </div>
)

export default FavoriteList

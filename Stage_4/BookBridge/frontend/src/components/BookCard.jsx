import React from 'react'

const BookCard = ({ book }) => (
  <div className="book-card">
    <img src={book.cover || '/default-cover.jpg'} alt={book.title} />
    <h3>{book.title}</h3>
    <p>{book.author}</p>
    <button>Add to Favorites</button>
  </div>
)

export default BookCard

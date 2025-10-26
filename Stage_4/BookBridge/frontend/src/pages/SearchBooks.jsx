import React, { useState } from 'react'
import { getBooks } from '../services/api'
import BookCard from '../components/BookCard'

const SearchBooks = () => {
  const [query, setQuery] = useState('')
  const [books, setBooks] = useState([])

  const handleSearch = async (e) => {
    e.preventDefault()
    const data = await getBooks(query)
    setBooks(data)
  }

  return (
    <div className="search-page">
      <form onSubmit={handleSearch}>
        <input type="text" placeholder="Search for a book..." value={query} onChange={(e) => setQuery(e.target.value)} />
        <button type="submit">Search</button>
      </form>
      <div className="book-list">
        {books.map((book, i) => <BookCard key={i} book={book} />)}
      </div>
    </div>
  )
}

export default SearchBooks

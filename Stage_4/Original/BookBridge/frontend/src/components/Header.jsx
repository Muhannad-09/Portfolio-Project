import React from 'react'
import { Link } from 'react-router-dom'

export default function Header() {
  return (
    <header style={{ padding: '1rem', backgroundColor: '#f5f5f5' }}>
      <h1>📚 BookBridge</h1>
      <nav>
        <Link to="/">Home</Link>
      </nav>
    </header>
  )
}

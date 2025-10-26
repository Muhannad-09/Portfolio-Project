import React from 'react'
import { Link } from 'react-router-dom'
import './Navbar.css'

const Navbar = () => (
  <nav className="navbar">
    <div className="logo">📘 BookBridge</div>
    <ul className="nav-links">
      <li><Link to="/">Home</Link></li>
      <li><Link to="/favorites">Favorites</Link></li>
      <li><Link to="/login">Login</Link></li>
    </ul>
  </nav>
)

export default Navbar

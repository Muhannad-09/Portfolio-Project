import React from "react";

const BookCard = ({ book }) => {
  return (
    <div
      className="book-card"
      style={{
        background: "white",
        borderRadius: "10px",
        padding: "1rem",
        boxShadow: "0 2px 6px rgba(0,0,0,0.1)",
        textAlign: "center",
      }}
    >
      <img
        src={book.cover_url || "https://via.placeholder.com/150"}
        alt={book.title}
        style={{
          width: "100%",
          height: "220px",
          objectFit: "cover",
          borderRadius: "8px",
        }}
      />
      <h3 style={{ marginTop: "0.75rem" }}>{book.title}</h3>
      <p style={{ color: "#555", marginBottom: "0.5rem" }}>
        {book.author || "Unknown Author"}
      </p>
      {book.description && (
        <p
          style={{
            fontSize: "0.9rem",
            color: "#666",
            lineHeight: "1.3",
            maxHeight: "4.5em",
            overflow: "hidden",
            textOverflow: "ellipsis",
          }}
        >
          {book.description}
        </p>
      )}
    </div>
  );
};

export default BookCard;

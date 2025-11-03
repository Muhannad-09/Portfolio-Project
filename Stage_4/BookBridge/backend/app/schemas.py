def book_to_dict(book):
    return {
        "id": book.id,
        "title": book.title,
        "author": book.author,
        "description": book.description,
        "category": book.category,
        "cover_url": book.cover_url,
        "created_at": book.created_at.isoformat()
    }

def review_to_dict(review):
    return {
        "id": review.id,
        "user_id": review.user_id,
        "book_id": review.book_id,
        "rating": review.rating,
        "comment": review.comment,
        "created_at": review.created_at.isoformat()
    }

def user_to_dict(user):
    return {
        "id": user.id,
        "username": user.username,
        "role": user.role,
        "created_at": user.created_at.isoformat()
    }


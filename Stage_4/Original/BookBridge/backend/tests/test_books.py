import json
from app import create_app, db

def test_list_books():
    app = create_app()
    client = app.test_client()

    with app.app_context():
        db.create_all()
        from app.models import Book
        b = Book(title="Test Book", author="Author X")
        db.session.add(b)
        db.session.commit()

    resp = client.get("/api/v1/books/")
    assert resp.status_code == 200
    data = resp.get_json()
    assert isinstance(data, list)
    assert any(book["title"] == "Test Book" for book in data)


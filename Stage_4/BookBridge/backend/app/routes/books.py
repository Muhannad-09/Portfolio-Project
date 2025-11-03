from flask import Blueprint, request, jsonify
from .. import db
from ..models import Book
from ..schemas import book_to_dict
from ..utils import admin_required
from flask_jwt_extended import jwt_required

books_bp = Blueprint("books", __name__)

@books_bp.route("/", methods=["GET"])
def list_books():
    q = request.args.get("q")
    category = request.args.get("category")
    query = Book.query
    if q:
        query = query.filter(Book.title.ilike(f"%{q}%"))
    if category:
        query = query.filter_by(category=category)
    books = query.order_by(Book.created_at.desc()).all()
    return jsonify([book_to_dict(b) for b in books])

@books_bp.route("/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = Book.query.get_or_404(book_id)
    return jsonify(book_to_dict(book))

@books_bp.route("/", methods=["POST"])
@admin_required
def create_book():
    data = request.get_json() or {}
    title = data.get("title")
    if not title:
        return jsonify({"msg": "title required"}), 400
    book = Book(
        title=title,
        author=data.get("author"),
        description=data.get("description"),
        category=data.get("category"),
        cover_url=data.get("cover_url")
    )
    db.session.add(book)
    db.session.commit()
    return jsonify(book_to_dict(book)), 201

@books_bp.route("/<int:book_id>", methods=["PUT"])
@admin_required
def update_book(book_id):
    book = Book.query.get_or_404(book_id)
    data = request.get_json() or {}
    for field in ("title", "author", "description", "category", "cover_url"):
        if field in data:
            setattr(book, field, data[field])
    db.session.commit()
    return jsonify(book_to_dict(book))

@books_bp.route("/<int:book_id>", methods=["DELETE"])
@admin_required
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({"msg": "deleted"}), 200


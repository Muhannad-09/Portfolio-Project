from flask import Blueprint, request, jsonify
from .. import db
from ..models import Review, Book, User
from ..schemas import review_to_dict
from flask_jwt_extended import jwt_required, get_jwt_identity

reviews_bp = Blueprint("reviews", __name__)

@reviews_bp.route("/book/<int:book_id>", methods=["GET"])
def list_reviews(book_id):
    reviews = Review.query.filter_by(book_id=book_id).order_by(Review.created_at.desc()).all()
    return jsonify([review_to_dict(r) for r in reviews])

@reviews_bp.route("/book/<int:book_id>", methods=["POST"])
@jwt_required()
def create_review(book_id):
    user_id = get_jwt_identity()
    data = request.get_json() or {}
    try:
        rating = int(data.get("rating", 0))
    except:
        rating = 0
    if rating < 1 or rating > 5:
        return jsonify({"msg": "rating must be 1-5"}), 400

    if not Book.query.get(book_id):
        return jsonify({"msg": "book not found"}), 404

    review = Review(user_id=user_id, book_id=book_id, rating=rating, comment=data.get("comment"))
    db.session.add(review)
    db.session.commit()
    return jsonify(review_to_dict(review)), 201

@reviews_bp.route("/<int:review_id>", methods=["DELETE"])
@jwt_required()
def delete_review(review_id):
    user_id = get_jwt_identity()
    review = Review.query.get_or_404(review_id)
    # allow delete if author or admin
    from ..models import User
    user = User.query.get(user_id)
    if review.user_id != user_id and user.role != "admin":
        return jsonify({"msg": "not allowed"}), 403
    db.session.delete(review)
    db.session.commit()
    return jsonify({"msg": "deleted"}), 200


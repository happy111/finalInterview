from flask import Blueprint, request, jsonify
from services.user_service import UserService

user_bp = Blueprint("user_bp", __name__)

@user_bp.route("/users", methods=["GET"])
def get_users():
    users = UserService.get_all_users()
    return jsonify([u.as_dict() for u in users])


@user_bp.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = UserService.get_user_by_id(user_id)
    return jsonify(user.as_dict()) if user else ("User not found", 404)


@user_bp.route("/users", methods=["POST"])
def create_user():
    data = request.json
    user = UserService.create_user(data["name"], data["email"])
    return jsonify(user.as_dict()), 201


@user_bp.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.json
    user = UserService.update_user(user_id, data["name"], data["email"])
    return jsonify(user.as_dict()) if user else ("User not found", 404)


@user_bp.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    deleted = UserService.delete_user(user_id)
    return ("User deleted", 200) if deleted else ("User not found", 404)

from flask import Blueprint, request, jsonify
from models.startup_model import startup
from views.startup_view import render_startup_list, render_startup_detail

startup_bp = Blueprint("startup", __name__)


@startup_bp.route("/startup", methods=["GET"])
def get_startup():
    startup = startup.get_all()
    return jsonify(render_startup_list(startup))



@startup_bp.route("/startup/<int:id>", methods=["GET"])
def get_startup(id):
    startup = startup.get_by_id(id)
    if startup:
        return jsonify(render_startup_detail(startup))
    return jsonify({"error": "startup no encontrado"}), 404


@startup_bp.route("/startup", methods=["POST"])
def create_startup():
    data = request.json
    title = data.get("title")
    descripcion = data.get("descripcion")
    status = data.get("status")
    created_at = data.get("create_at")
    assigned_to = data.get("assigned_to")
    
    if not title or not descripcion or status or created_at or assigned_to is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    startup = startup(title=title, descripcion=descripcion, status= status, assigned_to=assigned_to, age=age)
    startup.save()

    return jsonify(render_startup_detail(startup)), 201


@startup_bp.route("/startup/<int:id>", methods=["PUT"])
def update_startup(id):
    startup = startup.get_by_id(id)

    if not startup:
        return jsonify({"error": "startup no encontrado"}), 404

    data = request.json
    title = data.get("title")
    descripcion = data.get("descripcion")
    status = data.get("status")
    created_at = data.get("created_at")
    assigned_to = data.get("assigned_to")

    startup.update(title=title, descripcion=descripcion, status=status, created_at=created_at, assigned_to=assigned_to)

    return jsonify(render_startup_detail(startup))


@startup_bp.route("/startup/<int:id>", methods=["DELETE"])
def delete_startup(id):
    startup = startup.get_by_id(id)

    if not startup:
        return jsonify({"error": "Animal no encontrado"}), 404

    startup.delete()

    
    return "", 204




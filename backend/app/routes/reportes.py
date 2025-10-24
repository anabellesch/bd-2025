from flask import Blueprint, request, jsonify

reports_bp = Blueprint('reports', __name__)

@reports_bp.route('/most_reserved_rooms', methods=['GET'])
def most_reserved_rooms():
    # TODO: conectar con MySQL y hacer query
    return jsonify({"report": "Salas más reservadas"})

@reports_bp.route('/turns_most_demanded', methods=['GET'])
def turns_most_demanded():
    # TODO: conectar con MySQL y hacer query
    return jsonify({"report": "Turnos más demandados"})
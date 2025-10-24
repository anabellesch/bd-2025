from flask import Blueprint, request, jsonify
import mysql.connector
import os

participants_bp = Blueprint('participants', __name__)

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        database=os.getenv("DB_NAME"),
        port=int(os.getenv("DB_PORT"))
    )

# GET todos los participantes
@participants_bp.route('/', methods=['GET'])
def get_participants():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM participante")
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(results)

# POST crear participante
@participants_bp.route('/', methods=['POST'])
def create_participant():
    data = request.json
    ci = data.get('ci')
    nombre = data.get('nombre')
    apellido = data.get('apellido')
    email = data.get('email')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO participante (ci, nombre, apellido, email) VALUES (%s, %s, %s, %s)",
        (ci, nombre, apellido, email)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Participante creado"}), 201
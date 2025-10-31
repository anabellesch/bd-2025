from flask import Blueprint, request, jsonify
import mysql.connector
import os

sanciones_bp = Blueprint('sanciones', __name__)

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        database=os.getenv("DB_NAME"),
        port=int(os.getenv("DB_PORT"))
    )

@sanciones_bp.route('/', methods=['GET'])
def get_sanctions():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM sancion_participante")
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(results)

@sanciones_bp.route('/', methods=['POST'])
def create_sanction():
    data = request.json
    ci_participante = data.get('ci_participante')
    fecha_inicio = data.get('fecha_inicio')
    fecha_fin = data.get('fecha_fin')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO sancion_participante (ci_participante, fecha_inicio, fecha_fin) VALUES (%s, %s, %s)",
        (ci_participante, fecha_inicio, fecha_fin)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Sanción creada"}), 201
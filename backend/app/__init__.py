from flask import Flask
from flask_cors import CORS
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

def create_app():
    app = Flask(__name__)
    
    # Configuración de la base de datos
    app.config['MYSQL_HOST'] = os.getenv('DB_HOST')
    app.config['MYSQL_USER'] = os.getenv('DB_USER')
    app.config['MYSQL_PASSWORD'] = os.getenv('DB_PASS')
    app.config['MYSQL_DB'] = os.getenv('DB_NAME')
    app.config['MYSQL_PORT'] = int(os.getenv('DB_PORT', 3306))

    # Habilitar CORS para permitir peticiones desde frontend
    CORS(app)

    # Importar y registrar blueprints
    from app.routes.participantes import participantes_bp
    from app.routes.salas import salas_bp
    from app.routes.reservas import reservas_bp
    from app.routes.sanciones import sanciones_bp
    from app.routes.reportes import reportes_bp

    app.register_blueprint(participantes_bp, url_prefix='/participantes')
    app.register_blueprint(salas_bp, url_prefix='/salas')
    app.register_blueprint(reservas_bp, url_prefix='/reservas')
    app.register_blueprint(sanciones_bp, url_prefix='/sanciones')
    app.register_blueprint(reportes_bp, url_prefix='/reportes')

    return app

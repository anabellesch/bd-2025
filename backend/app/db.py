from flask import Flask
from flask_cors import CORS
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

def create_app():
    app = Flask(__name__)
    
    # Configuración de la aplicación
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')
    app.config['JSON_AS_ASCII'] = False  # Para caracteres especiales en español
    
    # Habilitar CORS para permitir peticiones desde frontend
    CORS(app, resources={
        r"/*": {
            "origins": ["http://localhost:3000", "http://localhost:5173"],
            "methods": ["GET", "POST", "PUT", "DELETE"],
            "allow_headers": ["Content-Type"]
        }
    })

    # Importar y registrar blueprints
    from app.routes.participantes import participantes_bp
    from app.routes.salas import salas_bp
    from app.routes.reservas import reservas_bp
    from app.routes.sanciones import sanciones_bp
    from app.routes.reportes import reportes_bp

    app.register_blueprint(participantes_bp, url_prefix='/api/participantes')
    app.register_blueprint(salas_bp, url_prefix='/api/salas')
    app.register_blueprint(reservas_bp, url_prefix='/api/reservas')
    app.register_blueprint(sanciones_bp, url_prefix='/api/sanciones')
    app.register_blueprint(reportes_bp, url_prefix='/api/reportes')

    # Ruta de salud (health check)
    @app.route('/api/health')
    def health():
        return {"status": "ok", "message": "API funcionando correctamente"}

    # Manejador de errores 404
    @app.errorhandler(404)
    def not_found(error):
        return {"error": "Endpoint no encontrado"}, 404

    # Manejador de errores 500
    @app.errorhandler(500)
    def internal_error(error):
        return {"error": "Error interno del servidor"}, 500

    return app
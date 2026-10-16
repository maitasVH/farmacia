from flask import Flask, jsonify
from config import Config
from controllers import api, vistas
from models import db


def create_app():
    # Tu carpeta se llama "template" (sin la "s"), por eso se indica aquí
    app = Flask(__name__, template_folder="template", static_folder="static")
    app.config.from_object(Config)
 
    db.init_app(app)
    app.register_blueprint(vistas)
    app.register_blueprint(api)
 
    @app.errorhandler(404)
    def no_encontrado(_):
        return jsonify({"error": "Recurso no encontrado"}), 404
 
    return app
 
 
app = create_app()
 
if __name__ == "__main__":
    app.run(debug=True)
 
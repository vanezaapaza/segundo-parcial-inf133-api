from flask import Flask
from controllers.startup_controller import startup_bp
from flask_swagger_ui import get_swaggerui_blueprint
from database import db

app = Flask(__name__)

SWAGGER_URL = "/api/docs"  # Ruta para servir Swagger UI
API_URL = "/static/openapi.yaml"  # Ruta de tu archivo OpenAPI/Swagger
swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL, API_URL, config={"app_name": "StarUp API"}
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///startup.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db.init_app(app)

app.register_blueprint(startup_bp, url_prefix="/api")

# Crea las tablas si no existen
with app.app_context():
    db.create_all()

# Ejecuta la aplicación
if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from config import Config
from database import db
from auth import auth_bp
from routes import routes_bp

app = Flask(__name__)
app.config.from_object(Config)

# Inicializar componentes
db.init_app(app)
jwt = JWTManager(app)

# Registrar Blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(routes_bp, url_prefix='/api')

# Crear base de datos
with app.app_context():
    db.create_all()

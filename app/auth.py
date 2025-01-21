from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, Usuario
from datetime import timedelta

auth_bp = Blueprint('auth', __name__)

# Registro de usuario
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    hashed_password = generate_password_hash(data['password'])
    usuario = Usuario(nombre=data['nombre'], email=data['email'], password=hashed_password)
    
    db.session.add(usuario)
    db.session.commit()
    
    return jsonify({'message': 'Usuario registrado exitosamente'}), 201

# Inicio de sesión
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    usuario = Usuario.query.filter_by(email=data['email']).first()

    if usuario and check_password_hash(usuario.password, data['password']):
        access_token = create_access_token(identity=usuario.id, expires_delta=timedelta(hours=1))
        return jsonify({'access_token': access_token})

    return jsonify({'message': 'Credenciales incorrectas'}), 401

# Ruta protegida (para probar autenticación)
@auth_bp.route('/perfil', methods=['GET'])
@jwt_required()
def perfil():
    usuario_id = get_jwt_identity()
    usuario = Usuario.query.get(usuario_id)
    return jsonify({'nombre': usuario.nombre, 'email': usuario.email})

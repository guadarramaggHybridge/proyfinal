from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db, Pregunta, Respuesta

routes_bp = Blueprint('routes', __name__)

# Crear pregunta (protegido con JWT)
@routes_bp.route('/preguntas', methods=['POST'])
@jwt_required()
def crear_pregunta():
    data = request.json
    usuario_id = get_jwt_identity()
    
    pregunta = Pregunta(titulo=data['titulo'], contenido=data['contenido'], usuario_id=usuario_id)
    db.session.add(pregunta)
    db.session.commit()

    return jsonify({'message': 'Pregunta creada'}), 201

# Listar preguntas
@routes_bp.route('/preguntas', methods=['GET'])
def listar_preguntas():
    preguntas = Pregunta.query.all()
    return jsonify([{'id': p.id, 'titulo': p.titulo, 'contenido': p.contenido} for p in preguntas])

# Agregar respuesta (protegido con JWT)
@routes_bp.route('/respuestas/<int:pregunta_id>', methods=['POST'])
@jwt_required()
def responder_pregunta(pregunta_id):
    data = request.json
    usuario_id = get_jwt_identity()

    respuesta = Respuesta(contenido=data['contenido'], usuario_id=usuario_id, pregunta_id=pregunta_id)
    db.session.add(respuesta)
    db.session.commit()

    return jsonify({'message': 'Respuesta agregada'}), 201

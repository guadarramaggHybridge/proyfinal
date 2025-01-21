from database import db
from datetime import datetime

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)

class Pregunta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(255), nullable=False)
    contenido = db.Column(db.Text, nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)

class Respuesta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    contenido = db.Column(db.Text, nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    pregunta_id = db.Column(db.Integer, db.ForeignKey('pregunta.id'), nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)

class Voto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    respuesta_id = db.Column(db.Integer, db.ForeignKey('respuesta.id'), nullable=False)
    tipo = db.Column(db.String(10), nullable=False)  # "upvote" o "downvote"

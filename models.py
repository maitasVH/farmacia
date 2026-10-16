from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()
 
 
class Medicamento(db.Model):
    __tablename__ = "medicamentos"
 
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(110), nullable=False)
    categoria = db.Column(db.String(110), nullable=False)
    cantidad = db.Column(db.String(110), nullable=False)
    dosis = db.Column(db.String(110), nullable=False)
    # En tu base de datos la columna se llama "presio"; aquí se expone como "precio"
    precio = db.Column("presio", db.Integer)
 
    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "cantidad": self.cantidad,
            "dosis": self.dosis,
            "precio": self.precio,
        }
 
 
class Empleado(db.Model):
    __tablename__ = "empleados"
 
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(110), nullable=False)
    apellido = db.Column(db.String(110), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    especialidad = db.Column(db.String(110), nullable=False)
    asiste = db.Column(db.String(110), nullable=False)
 
    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "edad": self.edad,
            "especialidad": self.especialidad,
            "asiste": self.asiste,
        }
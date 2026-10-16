from flask import Blueprint, jsonify, render_template, request
from models import Empleado, Medicamento, db


vistas = Blueprint("vistas", __name__)
api = Blueprint("api", __name__, url_prefix="/api")
 
CAMPOS_MEDICAMENTO = ["nombre", "categoria", "cantidad", "dosis", "precio"]
CAMPOS_EMPLEADO = ["nombre", "apellido", "edad", "especialidad", "asiste"]
 
 
def faltantes(datos, campos):
    if not datos:
        return campos
    return [c for c in campos if c not in datos or datos[c] in (None, "")]
 
 
# ---------------------------------------------------------------- VISTAS HTML
@vistas.route("/")
def index():
    return render_template("index.html")
 
 
@vistas.route("/administracion")
def administracion():
    medicamentos = Medicamento.query.all()
    return render_template("administración.html", medicamentos=medicamentos)


@vistas.route("/empleados")
def empleados():
    empleados = Empleado.query.all()
    return render_template("empleados.html", empleados=empleados)


# ------------------------------------------------------------ API MEDICAMENTOS
@api.route("/medicamentos", methods=["GET"])
def listar_medicamentos():
    return jsonify([m.to_dict() for m in Medicamento.query.all()])
 
 
@api.route("/medicamentos/<int:id>", methods=["GET"])
def obtener_medicamento(id):
    return jsonify(Medicamento.query.get_or_404(id).to_dict())
 
 
@api.route("/medicamentos", methods=["POST"])
def crear_medicamento():
    datos = request.get_json(silent=True)
    falta = faltantes(datos, CAMPOS_MEDICAMENTO)
    if falta:
        return jsonify({"error": "Faltan campos", "campos": falta}), 400
 
    medicamento = Medicamento(
        nombre=datos["nombre"],
        categoria=datos["categoria"],
        cantidad=str(datos["cantidad"]),
        dosis=datos["dosis"],
        precio=int(datos["precio"]),
    )
    db.session.add(medicamento)
    db.session.commit()
    return jsonify(medicamento.to_dict()), 201
 
 
@api.route("/medicamentos/<int:id>", methods=["PUT"])
def actualizar_medicamento(id):
    medicamento = Medicamento.query.get_or_404(id)
    datos = request.get_json(silent=True) or {}
    for campo in CAMPOS_MEDICAMENTO:
        if campo in datos:
            valor = int(datos[campo]) if campo == "precio" else str(datos[campo])
            setattr(medicamento, campo, valor)
    db.session.commit()
    return jsonify(medicamento.to_dict())
 
 
@api.route("/medicamentos/<int:id>", methods=["DELETE"])
def eliminar_medicamento(id):
    medicamento = Medicamento.query.get_or_404(id)
    db.session.delete(medicamento)
    db.session.commit()
    return jsonify({"mensaje": "Medicamento eliminado"})
 
 
# --------------------------------------------------------------- API EMPLEADOS
@api.route("/empleados", methods=["GET"])
def listar_empleados():
    return jsonify([e.to_dict() for e in Empleado.query.all()])
 
 
@api.route("/empleados/<int:id>", methods=["GET"])
def obtener_empleado(id):
    return jsonify(Empleado.query.get_or_404(id).to_dict())
 
 
@api.route("/empleados", methods=["POST"])
def crear_empleado():
    datos = request.get_json(silent=True)
    falta = faltantes(datos, CAMPOS_EMPLEADO)
    if falta:
        return jsonify({"error": "Faltan campos", "campos": falta}), 400
 
    empleado = Empleado(
        nombre=datos["nombre"],
        apellido=datos["apellido"],
        edad=int(datos["edad"]),
        especialidad=datos["especialidad"],
        asiste=datos["asiste"],
    )
    db.session.add(empleado)
    db.session.commit()
    return jsonify(empleado.to_dict()), 201
 
 
@api.route("/empleados/<int:id>", methods=["PUT"])
def actualizar_empleado(id):
    empleado = Empleado.query.get_or_404(id)
    datos = request.get_json(silent=True) or {}
    for campo in CAMPOS_EMPLEADO:
        if campo in datos:
            valor = int(datos[campo]) if campo == "edad" else str(datos[campo])
            setattr(empleado, campo, valor)
    db.session.commit()
    return jsonify(empleado.to_dict())
 
 
@api.route("/empleados/<int:id>", methods=["DELETE"])
def eliminar_empleado(id):
    empleado = Empleado.query.get_or_404(id)
    db.session.delete(empleado)
    db.session.commit()
    return jsonify({"mensaje": "Empleado eliminado"})
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def root ():
    return "Welcome"

from Docentes import Docentes 

@app.route("/Docentes")
def getDocentes():
    return jsonify (Docentes)


## METODO PARA BUSCAR DOCENTE
@app.route("/Docentes/<string:docente_name>")
def getdocente(docente_name):
    docentefound = [docente for docente in Docentes if docente ["Nombre"] == docente_name]
    if (len(docentefound) > 0):
        return jsonify ({"Docentes": docentefound[0]})

## METODO PARA AGREGAR DOCENTE
@app.route("/Docentes", methods=["POST"])
def adddocente():
    docente = request.json
    Docentes.append(docente)
    return jsonify({"mensaje": "Docente agregado satisfactoriamente", "docentes":Docentes})

## METODO PARA Actualizar DOCENTE
@app.route("/Docentes/<string:docente_name>", methods=["PATCH"])
def patchdocente(docente_name):
    docente_found = [docente for docente in Docentes if docente["Nombre"] == docente_name]
    if len(docente_found) > 0:
        docente_actualizado = {}
        for key, value in request.json.items():
            docente_actualizado[key] = value
        docente_found[0].update(docente_actualizado)
        return jsonify({
            "mensaje": "Docente Actualizado satisfactoriamente",
            "Docentes": docente_found[0]
})
    
## METODO PARA ELIMINAR DOCENTE
@app.route("/Docentes/<string:docente_name>", methods=["DELETE"])
def elimindocente(docente_name):
    docentesfound = [docente for docente in Docentes if docente["Nombre"] == docente_name]
    if len(docentesfound) > 0:
        Docentes.remove(docentesfound[0])
        return jsonify({
            "mensaje": "El docente Eliminado",
            "Docentes": Docentes
})

if __name__ == "__main__":
    app.run(debug=True)

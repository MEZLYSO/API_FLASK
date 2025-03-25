from flask import Flask, jsonify, request

app = Flask("__name__")


# Lista de items
frameworks = [
    {
        "id": 1,
        "name": "Flask"
    },
    {
        "id": 2,
        "name": "NodeJS"
    }
]

# Ruta inicial


@app.route("/")
def index():
    return "API"


# Retorna datos completos del JSON
@app.route("/items", methods=["GET"])
def view_frameworks():
    return jsonify(frameworks)

# Obtener un elemento a partir del nombre de un elemento de JSON


@app.route("/items/<string:name>", methods=["GET"])
def view_framework(name):
    framework = []
    for f in frameworks:
        if f["name"] == name:
            framework.append(f)
    return jsonify(framework[0])

# Me permite insertar elementos en mi lista


@app.route("/items", methods=["POST"])
def add_framework():
    # framework = request.json
    # Evitar ingreso de parametros fuera de los establecidos
    # Definicion de modelo para almacer los elementos en elemento
    framework = {
        "id": request.json['id'],
        "name": request.json['name']
    }

    frameworks.append(framework)

    return jsonify(framework)


# Edicion de elementos usando PUT
@app.route("/items/<int:id>", methods=["PUT"])
def update_framework(id):
    framework = [
        framework for framework in frameworks if framework["id"] == id]
    framework = framework[0]
    framework["id"] = request.json["id"]
    framework["name"] = request.json["name"]
    return jsonify(framework)


if __name__ == "__main__":
    app.run()

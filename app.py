from flask import Flask, jsonify
import json

app = Flask(__name__)

def Productos():
    with open('Api/Api.json') as f:
        productos = json.load(f)
    return productos

def Busqueda(nombre):
    productos = Productos()
    for producto in productos:
        if producto['nombre'].lower() == nombre.lower():
            return producto  # Retorna el primer producto que coincida
    return {"mensaje": "Producto no encontrado o se más especifico"}

@app.route('/', methods=['GET'])
def hello():
    return jsonify(Productos())

@app.route('/busqueda/<nombre>', methods=['GET'])  # Usamos GET para pasar parámetros en la URL
def Busquedas(nombre):
    return jsonify(Busqueda(nombre))


if __name__ == '__main__':
    app.run(debug=True)
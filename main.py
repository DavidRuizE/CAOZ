from flask import Flask, jsonify

app = Flask(__name__)

# Datos de ejemplo de clientes y productos
clientes = [
    {"id": 1, "nombre_cliente": "Valeria Correa ", "productos": [
        {"id_producto": 6, "nombre": "CUT CROP TOP AMARILLO", "precio": 85000, "talla": "M", "enlace": "/producto/6", "cantidad_disponible_M": 4},
        {"id_producto": 8, "nombre": "BUSO ROUND NECK MORADO", "precio": 120000, "talla": "L", "enlace": "/producto/8", "cantidad_disponible_L": 43}
    ]},
    {"id": 2, "nombre_cliente": "Daniel Pineda", "productos": [
        {"id_producto": 10, "nombre": "BASIC TREE RIB VERDE", "precio": 85000, "talla": "S", "enlace": "/producto/10", "cantidad_disponible_S": 4}
    ]},
    {"id": 3, "nombre_cliente": "Julián Valencia ", "productos": [
        {"id_producto": 2, "nombre": "CATA USME SHORT", "precio": 160000, "talla": "XL", "enlace": "/producto/2", "cantidad_disponible_XL": 1},
        {"id_producto": 8, "nombre": "BUSO ROUND NECK MORADO", "precio": 120000, "talla": "M", "enlace": "/producto/8", "cantidad_disponible_M": 11}
    ]},
    {"id": 4, "nombre_cliente": "Anderson Castaño", "productos": [
        {"id_producto": 11, "nombre": "COLLEGE BLUE T-SHIRT", "precio": 165000, "talla": "L", "enlace": "/producto/11", "cantidad_disponible_L": 2}
    ]},
    {"id": 5, "nombre_cliente": "Maria José Ortiz", "productos": [
        {"id_producto": 9, "nombre": "HOODIE CROP ENRESORTADO BLANCO", "precio": 190000, "talla": "S", "enlace": "/producto/9", "cantidad_disponible_S": 3},
        {"id_producto": 11, "nombre": "COLLEGE BLUE T-SHIRT", "precio": 165000, "talla": "XL", "enlace": "/producto/11", "cantidad_disponible_XL": 2}
    ]},
    {"id": 6, "nombre_cliente": " Diana Galvis", "productos": [
        {"id_producto": 7, "nombre": "JEAN CARPENTER MUJER 369 AZUL", "precio": 190000, "talla": "M", "enlace": "/producto/7", "cantidad_disponible_M": 3}
    ]},
    {"id": 7, "nombre_cliente": "David Osorio", "productos": [
        {"id_producto": 2, "nombre": "CATA USME SHORT", "precio": 160000, "talla": "L", "enlace": "/producto/2", "cantidad_disponible_L": 7},
        {"id_producto": 3, "nombre": "CATA USME PULLOVER", "precio": 220.000, "talla": "S", "enlace": "/producto/3", "cantidad_disponible_S": 23}
    ]},
    {"id": 8, "nombre_cliente": "Juan Arriola ", "productos": [
        {"id_producto": 3, "nombre": "CATA USME PULLOVER", "precio": 220000, "talla": "M", "enlace": "/producto/3", "cantidad_disponible_M": 3}
    ]},
    {"id": 9, "nombre_cliente": "Ricardo Sánchez", "productos": [
        {"id_producto": 2, "nombre": "CATA USME SHORT", "precio": 160000, "talla": "XL", "enlace": "/producto/2", "cantidad_disponible_XL": 1},
        {"id_producto": 11, "nombre": "COLLEGE BLUE T-SHIRT", "precio": 165000, "talla": "S", "enlace": "/producto/11", "cantidad_disponible_S": 3}
    ]},
    {"id": 10, "nombre_cliente": "Sofia londoño ", "productos": [
        {"id_producto": 4, "nombre": "CATA USME HOODIE", "precio": 210000, "talla": "L", "enlace": "/producto/4", "cantidad_disponible_L": 4}
    ]},
    {"id": 11, "nombre_cliente": "Matías Vecino", "productos": [
        {"id_producto": 9, "nombre": "HOODIE CROP ENRESORTADO BLANCO", "precio": 190000, "talla": "M", "enlace": "/producto/9", "cantidad_disponible_M": 4},
        {"id_producto": 4, "nombre": "CATA USME HOODIE", "precio": 210000, "talla": "XL", "enlace": "/producto/4", "cantidad_disponible_XL": 8}
    ]},
    {"id": 12, "nombre_cliente": "Andrés Mazo ", "productos": [
        {"id_producto": 5, "nombre": "CATA USME GRAY HOODIE", "precio": 260000, "talla": "S", "enlace": "/producto/5", "cantidad_disponible_S": 3}
    ]},
    {"id": 13, "nombre_cliente": " David González", "productos": [
        {"id_producto": 6, "nombre": "CUT CROP TOP AMARILLO", "precio": 85000, "talla": "L", "enlace": "/producto/6", "cantidad_disponible_L": 2},
        {"id_producto": 4, "nombre": "CATA USME HOODIE", "precio": 210000, "talla": "M", "enlace": "/productos/4", "cantidad_disponible_M": 3}
    ]},
    {"id": 14, "nombre_cliente": "Valentina Orrego", "productos": [
        {"id_producto": 4, "nombre": "CATA USME HOODIE", "precio": 210000, "talla": "XL", "enlace": "/producto/4", "cantidad_disponible_XL": 8}
    ]},
    {"id": 15, "nombre_cliente": "Carlos Bustamante", "productos": [
        {"id_producto": 7, "nombre": "JEAN CARPENTER MUJER 369 AZUL", "precio": 190000, "talla": "S", "enlace": "/producto/7", "cantidad_disponible_S": 2}
    ]}
]

@app.route('/clientes', methods=['GET'])
def obtener_clientes():
    return jsonify(clientes)

@app.route('/clientes/<int:id_cliente>', methods=['GET'])
def obtener_cliente(id_cliente):
    cliente = next((c for c in clientes if c["id"] == id_cliente), None)
    if cliente:
        return jsonify(cliente)
    else:
        return jsonify({"mensaje": "Cliente no encontrado"}), 404

@app.route('/clientes/<int:id_cliente>/productos/<int:id_producto>', methods=['GET'])
def obtener_producto_cliente(id_cliente, id_producto):
    cliente = next((c for c in clientes if c["id"] == id_cliente), None)
    if cliente:
        producto = next((p for p in cliente["productos"] if p["id_producto"] == id_producto), None)
        if producto:
            return jsonify(producto)
        else:
            return jsonify({"mensaje": "Producto no encontrado"}), 404
    else:
        return jsonify({"mensaje": "Cliente no encontrado"}), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)

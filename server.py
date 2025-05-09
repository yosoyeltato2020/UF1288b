from flask import Flask, request, jsonify

app = Flask(__name__)
mensajes = []  # Lista para almacenar los mensajes

@app.route("/", methods=["POST"])
def recibir_mensaje():
    """Recibe un mensaje de un cliente y lo retransmite a todos."""
    data = request.get_json()
    if "mensaje" in data:
        mensajes.append(data["mensaje"])
        respuesta = {
            "estado": "Mensaje recibido",
            "mensaje": data["mensaje"],
            "historial": mensajes  # Enviamos el historial de mensajes
        }
        return jsonify(respuesta), 200
    return jsonify({"error": "Mensaje no recibido"}), 400

@app.route("/", methods=["GET"])
def obtener_mensajes():
    """Devuelve todos los mensajes almacenados."""
    return jsonify({"mensajes": mensajes})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
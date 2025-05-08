from flask import Flask, request, jsonify

# Inicio de la aplicación
app = Flask(__name__)

# Ruta para recibir mensajes de clientes
@app.route('/')
def recibir_mensaje():
    # Obtener el mensaje del cliente
    mensaje = request.form.get("mensaje")

    if mensaje:
        print(f"Mensaje recibido: {mensaje}")
        return "Mensaje recibido con éxito", 200    
    else:
        return "No se recibió ningún mensaje", 400

# Ejecutar el servidor en el puerto 5000
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5051)

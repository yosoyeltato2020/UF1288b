import requests

url = "http://localhost:8080"

def enviar_mensaje(mensaje):
    """Envía un mensaje al servidor y recibe la confirmación."""
    datos = {"mensaje": mensaje}
    respuesta = requests.post(url, json=datos)
    print("Respuesta del servidor:", respuesta.json())

# Prueba enviando un mensaje
enviar_mensaje("¡Hola desde el cliente!")

# Obtener historial de mensajes
historial_respuesta = requests.get("http://localhost:8080")
print("Historial de mensajes:", historial_respuesta.json())

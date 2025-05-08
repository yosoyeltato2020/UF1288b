import requests
import json
SERVER_URL="http://192.168.1.18:5000/message"

def enviar_mensaje(mensaje):
    """
    Funcion para enviar un mensaje a la servidor y recibir una respuesta del servidor
    """
    
    try:
        data = {"mensaje": mensaje}

        response = requests.post(SERVER_URL, data=data)

        if response.status_code == 200:
            print("Mensaje enviado correctamente.")
            print("Respuesta del servidor:", response.text)
        else:
            print("Error al enviar el mensaje. Código de estado:", response.text)
            
    except Exception as e:
        print("Error:", e)
            
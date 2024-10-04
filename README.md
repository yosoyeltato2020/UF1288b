# UF1288 - Desarrollo de Componentes Software para Servicios de Comunicaciones

# Recuperación UF1288: Desarrollo de Componentes Software para Servicios de Comunicaciones

## Parte 1: Teoría (4 puntos)

1. Explica las diferencias entre el protocolo **TCP** y el protocolo **UDP**. ¿Cuándo elegirías uno sobre el otro?

2. Describe brevemente el modelo **cliente-servidor** y su importancia en el desarrollo de servicios de comunicaciones.

3. ¿Cuál es la diferencia entre una petición HTTP de tipo **GET** y una de tipo **POST**? Proporciona un caso de uso para cada una.

4. ¿Qué es una **API** y por qué es fundamental en el desarrollo de software para comunicaciones?
   
---

## Parte 2: Práctica (6 puntos)

Para esta parte, desarrollaremos y trabajaremos con una aplicación básica que gestiona mensajes entre clientes y un servidor. Asegurate de comitera, como mínimo, cada punto en un commit distinto. Como respuesta incluye el enlace al repositorio (público)

**Contexto:** Estás creando un pequeño servicio de chat donde varios clientes pueden enviar y recibir mensajes de texto. El servicio se ejecutará sobre el protocolo **HTTP**.

1. **Creación de un servidor HTTP (2 puntos)**
   a) Escribe un programa en el lenguaje de programación de tu elección que actúe como un servidor HTTP. El servidor debe:
   - Aceptar múltiples conexiones de clientes.
   - Recibir mensajes de texto de cada cliente.
   - Enviar una confirmación de recepción a cada cliente.

   *Incluye comentarios en el código para explicar cada parte.*

2. **Implementación de un cliente HTTP (1.5 puntos)**
   b) Escribe un programa que actúe como cliente HTTP, capaz de conectarse al servidor anterior, enviar un mensaje de texto y recibir la confirmación del servidor.

   *Incluye comentarios en el código.*

3. **Envío de mensajes entre clientes (1.5 puntos)**
   c) Modifica el servidor para que, cada vez que reciba un mensaje de un cliente, lo retransmita a todos los demás clientes conectados al servicio.

import json
import os

# Archivo donde se guardarán las preguntas y respuestas
archivo_conocimiento = "base_conocimiento.json"

# Función para cargar la base de conocimiento desde un archivo JSON o crearlo si no existe
def cargar_base_de_conocimiento():
    # Verificar si el archivo JSON ya existe
    if os.path.exists(archivo_conocimiento):
        # Si el archivo existe, cargarlo
        with open(archivo_conocimiento, "r") as archivo:
            return json.load(archivo)  # Cargar y devolver la base de conocimientos
    else:
        # Si no existe, crear una base de conocimiento inicial
        base_inicial = {
            "hola": "¡Hola! ¿Cómo estás?",
            "como estas?": "Estoy bien, ¿y tú?",
            "de que te gustaría hablar?": "Hablemos de lo que prefieras."
        }
        # Guardar la base inicial en un nuevo archivo JSON
        with open(archivo_conocimiento, "w") as archivo:
            json.dump(base_inicial, archivo)  # Guardar la base de conocimientos inicial
        return base_inicial

# Función para guardar la base de conocimiento en un archivo JSON
def guardar_base_de_conocimiento(base_de_conocimiento):
    with open(archivo_conocimiento, "w") as archivo:
        json.dump(base_de_conocimiento, archivo)  # Guardar la base de conocimientos en JSON

# Función para manejar el chat
def manejar_chat():
    base_de_conocimiento = cargar_base_de_conocimiento()  # Cargar la base de conocimientos

    while True:
        # Obtener input del usuario
        user_input = input("Tú: ").lower()

        # Verificar si el usuario quiere salir
        if user_input == "salir":
            print("Bot: ¡Hasta luego!")
            break

        # Buscar si la entrada está en la base de conocimiento
        if user_input in base_de_conocimiento:
            # Responder con la respuesta correspondiente
            print(f"Bot: {base_de_conocimiento[user_input]}")
        else:
            # Si no hay coincidencia, preguntar por la nueva respuesta
            print("Bot: No sé cómo responder a eso. ¿Cómo debería responder en el futuro?")
            nueva_respuesta = input("Tú (proporciona una respuesta): ")

            # Añadir la nueva pregunta/respuesta a la base de conocimiento
            base_de_conocimiento[user_input] = nueva_respuesta
            guardar_base_de_conocimiento(base_de_conocimiento)  # Guardar la base de conocimientos actualizada
            print(f"Bot: Gracias, ahora sé cómo responder '{user_input}'.")

# Ejecutar el chat
manejar_chat()

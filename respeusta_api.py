import requests
import tkinter as tk
from tkinter import ttk

def hacer_peticion_api(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza una excepción si la petición no fue exitosa
        return response.json()  # Devuelve la respuesta en formato JSON
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')

def buscar():
    query = entry.get()
    url = f'http://localhost:5000/busqueda/{query}'
    datos = hacer_peticion_api(url)
    result_text.set(datos)

# Crear la ventana principal
root = tk.Tk()
root.title("Buscador API")

# Crear un cuadro de texto para la entrada de búsqueda
entry = ttk.Entry(root, width=50)
entry.pack(pady=10)

# Crear un botón para realizar la búsqueda
button = ttk.Button(root, text="Buscar", command=buscar)
button.pack(pady=5)

# Crear una etiqueta para mostrar los resultados
result_text = tk.StringVar()
result_label = ttk.Label(root, textvariable=result_text, wraplength=400)
result_label.pack(pady=10)

# Iniciar el bucle principal de la aplicación
root.mainloop()
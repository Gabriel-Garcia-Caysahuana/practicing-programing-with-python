"""Instalación y Configuración de requests: Instala la librería requests en 
tu entorno de trabajo y realiza una simple solicitud HTTP GET a una página 
web de prueba para verificar que la instalación fue exitosa."""

import requests

path = "https://books.toscrape.com/index.html"


response = requests.get(path)
print(response.status_code)
print(response.text)

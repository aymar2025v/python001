import requests
respuesta = requests.get("https://github.com")
print("Estado de la conexión:", respuesta.status_code)

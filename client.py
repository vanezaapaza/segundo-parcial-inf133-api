import requests

# URL base de la API
BASE_URL = "http://localhost:5000/api"

# Definir los encabezados de la solicitud
headers = {"Content-Type": "application/json"}

url = f"{BASE_URL}/tareas"
nuevo_startup = {"title": "desarrollar", "descripcion": "", "status": "Felino", "created_at": "", "assigned_to":""}
response = requests.post(url, json=nuevo_startup, headers=headers)
print("Creando un nuevo startup:")
print(response.json())

startup_2 = {"title": "desarrollar", "descripcion": "", "status": "Felino", "created_at": "", "assigned_to":""}
response = requests.post(url, json=startup_2, headers=headers)
print("\nCreando el segundo startup:")
print(response.json())

url = f"{BASE_URL}/startup"
response = requests.get(url, headers=headers)
print("\nLista de startup:")
print(response.json())

url = f"{BASE_URL}/startup/1"
response = requests.get(url, headers=headers)
print("\nDetalles del startup con ID 1:")
print(response.json())

url = f"{BASE_URL}/startup/1"
datos_actualizacion = {"title": "desarrollar", "descripcion": "", "status": "Felino", "created_at": "", "assigned_to":""}
response = requests.put(url, json=datos_actualizacion, headers=headers)
print("\nActualizando el startup con ID 1:")
print(response.json())

url = f"{BASE_URL}/startup/1"
response = requests.delete(url, headers=headers)
print("\nEliminando el startup con ID 1:")
if response.status_code == 204:
    print(f"startup con ID 1 eliminado con éxito.")
else:
    print(f"Error: {response.status_code} - {response.text}")
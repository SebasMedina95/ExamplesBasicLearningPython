users = {
    "data": [
        {
            "uuid": "9bc8df28-53ea-4326-ab9e-635c5ceb6e54",
            "name": "Juan Sebastián Medina",
            "email": "juan.medina@example.com",
            "charge": "Desarrollador Backend",
            "salary": 8500000
        },
        {
            "uuid": "a7d3e19c-92ce-4e7b-a18d-1f84e2d6f302",
            "name": "Ana María López",
            "email": "ana.lopez@example.com",
            "charge": "Analista QA",
            "salary": 6000000
        },
        {
            "uuid": "f1b2c0e7-761a-45a5-acd9-44d4c1b81872",
            "name": "Carlos Rodríguez",
            "email": "carlos.rodriguez@example.com",
            "charge": "Scrum Master",
            "salary": 9500000
        },
        {
            "uuid": "d55f1e8b-2ffe-4d33-b823-f96d87c5b531",
            "name": "Laura Sánchez",
            "email": "laura.sanchez@example.com",
            "charge": "UX Designer",
            "salary": 7000000
        },
        {
            "uuid": "cc2a1f33-d92f-41d3-b210-944a8ec0a11b",
            "name": "Miguel Torres",
            "email": "miguel.torres@example.com",
            "charge": "DevOps Engineer",
            "salary": 10500000
        },
        {
            "uuid": "ef6d29ea-1b0c-4e33-8cd3-5e2b9f9f8912",
            "name": "Sofía Herrera",
            "email": "sofia.herrera@example.com",
            "charge": "Product Owner",
            "gender": "F",
            "salary": 9800000
        },
        {
            "uuid": "b1c8e4f2-7af4-43e3-8747-51fcd017f48a",
            "name": "Andrés Gómez",
            "email": "andres.gomez@example.com",
            "charge": "Data Engineer",
            "salary": 9200000
        }
    ],
    "meta": {
        "status": "OK",
        "date_query": "2025-12-02 23:45:10",
        "description": "Consulta de empleados activos en la organización"
    }
}

for user in users.get("data"):
    #print(user["name"], "-", user["charge"])
    print(user.get("name"), "-", user.get("charge"))

print("============================================================================================")
print(f"La consulta respondió el {users["meta"]["date_query"]} con estado {users["meta"]["status"]}")

# in me sirve para verificar si tengo algo en el diccionario
for user in users.get("data"):
    if "gender" in user:
        print(f"El género SÍ está como propiedad en {user['name']}")
    else:
        print(f"El género NO está como propiedad en {user['name']}")

print("===========================================================================================")
print("****************************************** ITEMS ******************************************")
# Trae los diccionarios
print(users.items())
print("===========================================================================================")
# Trae los values
print(users.values())

print()
print()
print()

# Caso de agregar
new_user = {
    "uuid": "2bc8df18-53ea-4326-ab9e-615c2ceb6e09",
    "name": "Celeste Meneses Danuvio",
    "email": "celeste.danuvio@example.com",
    "charge": "Desarrollador UX",
    "salary": 4100000
}

users.get("data").append(new_user)
for user in users.get("data"):
    print(user.get("name"), "-", user.get("charge"))

# Caso de eliminar
# El index se usa cuando necesitas modificar o eliminar un elemento de una lista accediéndolo por su posición dentro de la lista.
# Con esto evitamos errores
uuid_to_delete = "d55f1e8b-2ffe-4d33-b823-f96d87c5b531"

for index, user in enumerate(users["data"]):
    if user["uuid"] == uuid_to_delete:
        del users["data"][index]
        break

print()
print()
print()

for user in users.get("data"):
    print(user.get("name"), "-", user.get("charge"))

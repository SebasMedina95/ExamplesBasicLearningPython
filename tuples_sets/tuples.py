
# Ordenada
# Inmutable
# Permite duplicados
# Indexable
person = ("Juan", 28, "Desarrollador", "Backend", 2025)
print(person)

# Contar los elementos coincidentes
print(person.count(34))

# Buscar la posición exacta
print(person.index(2025))

new_person = ("Fabio", 69, "Product", "Owner", 2025)

# Un uso interesante:
ROLES_PERMITIDOS = ("ADMIN", "USER", "SUPPORT", "GUEST")

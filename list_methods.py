from dataclasses import dataclass

@dataclass
class Empleado:
    documento: str
    nombre: str
    salario: float
    cargo: str


empleados = [
    Empleado("1001", "Sebastián Medina", 4800000, "Backend Developer"),
    Empleado("1002", "Ana Torres", 5200000, "Frontend Developer"),
    Empleado("1003", "Luis Rojas", 6100000, "Fullstack Developer"),
    Empleado("1004", "María Gómez", 4500000, "QA Automation Engineer"),
    Empleado("1005", "Pedro Sánchez", 7000000, "DevOps Engineer"),
    Empleado("1006", "Daniel Castro", 3800000, "Jr Backend Developer"),
    Empleado("1007", "Juliana López", 8300000, "Cloud Architect"),
    Empleado("1008", "Camilo Ruiz", 4200000, "Data Engineer"),
    Empleado("1009", "Laura Hernández", 3900000, "Mobile Developer"),
    Empleado("1010", "Andrés Villa", 5600000, "Software Engineer")
]

for empl in empleados:
    print(empl.nombre)
    
print("=========================================")
menor_salario = min(empleados, key=lambda e: e.salario)
mayor_salario = max(empleados, key=lambda e: e.salario)

print(f"Menor salario: {menor_salario.nombre} - Con: {menor_salario.salario}")
print(f"Mayor salario: {mayor_salario.nombre} - Con: {mayor_salario.salario}")

nuevo_empleado = Empleado("4532","Monica Toro",11600000,"Scrum Master")
empleados.append(nuevo_empleado)
print("=========================================")

for empl in empleados:
    print(f"{empl.nombre}, {empl.cargo}")
    
# Eliminemos el menor salario
print("=========================================")
new_list = list(
    filter( lambda empl: empl.documento != menor_salario.documento, empleados )
)

for l in new_list:
    print(l.nombre)

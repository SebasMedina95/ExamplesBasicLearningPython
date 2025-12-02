from dataclasses import dataclass
import uuid

# Ejercicio elaborado de listas

# Clase de trabajo para la lista:
@dataclass
class ProductDTO:
    id: uuid.UUID
    name: str

# Lista
shopping_cart: list[ProductDTO] = [
    ProductDTO(uuid.uuid4(), "Procesador Intel Core i5"),
    ProductDTO(uuid.uuid4(), "Tarjeta madre ASUS Prime"),
    ProductDTO(uuid.uuid4(), "Memoria RAM 16GB DDR4"),
    ProductDTO(uuid.uuid4(), "SSD 1TB NVMe"),
    ProductDTO(uuid.uuid4(), "Fuente de poder 650W 80 Plus"),
    ProductDTO(uuid.uuid4(), "Tarjeta gráfica NVIDIA RTX 4060"),
    ProductDTO(uuid.uuid4(), "Gabinete ATX con ventiladores"),
    ProductDTO(uuid.uuid4(), "Cooler para CPU"),
    ProductDTO(uuid.uuid4(), "Monitor 24 pulgadas 144Hz"),
    ProductDTO(uuid.uuid4(), "Teclado mecánico RGB"),
]

# Método separado para validar el estado de la lista
def view_products():
    if not shopping_cart:
        print("El listado de productos está vacío")
        return
    for product in shopping_cart:
        print(f"- {product.name} | ID: {product.id}")
        
# Ciclo para trabajar la lógica
while True:

    print("\n--- MENÚ ---")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Mostrar la lista")
    print("4. Mostrar la lista ordenada")
    print("5. Buscar producto por ID")
    print("6. Contar productos del carrito")
    print("7. Vaciar el carrito")
    print("8. Salir")

    option = input("Elija una opción (1-8): ")

    # Validar que sea un número:
    if option.isdigit():
        option = int(option)
    else:
        print("❌ Opción inválida, por favor ingresa un número.")
        continue

    # Opción 1:
    if option == 1:
        new_product = input("Deme el nombre del producto")
        if new_product == None:
            print("❌ Nombre de producto inválido.")
        else:
            new_product = ProductDTO(uuid.uuid4(), new_product)
            shopping_cart.append(new_product)
            print(f"✔ Agregado: {new_product.name} (ID: {new_product.id})")
            
    
    # Salir
    if option == 8:
        shopping_cart.clear()
        print(f"😎 Saliendo del sistema ...")
        break

    # Opción Default
    if option <= 1 or option > 8:
        print("❌ Opción inválida, debe seleccionar una opción del 1 al 6.")
        continue
    

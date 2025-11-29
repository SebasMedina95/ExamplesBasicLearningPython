products_list = [
    {"name": "Laptop Lenovo", "quantity": 2, "price": 3200.50},
    {"name": "Mouse Logitech", "quantity": 5, "price": 89.99},
    {"name": "Teclado Mecánico Redragon", "quantity": 3, "price": 250.00},
    {"name": "Monitor LG 27''", "quantity": 1, "price": 1450.00},
    {"name": "Audífonos Sony WH-CH520", "quantity": 4, "price": 380.75},
]

count = 0
for prod in products_list:
    valid_price = prod["quantity"] * prod["price"]
    if valid_price >= 1450:
        count += 1
        
    print(f"Producto: {prod["name"]} -> Subtotal: {prod["quantity"] * prod["price"]}")

print("************************************************")
print(f"Cantidad de subtotales mayores a 1450: {count}")
print("************************************************")

# Supongamos subtotales mayores a 1500
new_product_list = list(
    filter( lambda p: p['quantity']*p['price'] > 1500 , products_list)
)

for resp in new_product_list:
    print(resp['name']);


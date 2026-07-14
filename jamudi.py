# 1
creaar_inventario = [  
    {"nombre": "Harina", "categoria": "Alimentos", "precio": 2.5},
    {"nombre": "Azúcar", "categoria": "Alimentos", "precio": 1.5},
    {"nombre": "coleto", "categoria": "limpieza", "precio": 3.0} 
    ]


# 3
def buscar_producto(inventario, codigo):
    try:
        codigo = int(codigo)
    except ValueError:
        print("Error: El código del producto debe ser un número entero.")
        return None

    if codigo in inventario:
        return inventario[codigo]
    else:
        print(f"Producto con código {codigo} no encontrado.")
        return None
    
# 2

def buscar_producto(inventario, codigo):
    try:
        codigo = int(codigo)
    except ValueError:
        print("Error: El código del producto debe ser un número entero.")
        return None

    if codigo in inventario:
        return inventario[codigo]
    else:
        print(f"Producto con código {codigo} no encontrado.")
        return None
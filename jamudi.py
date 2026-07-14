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
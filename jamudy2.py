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
    
#4
def estadisticas(inventario):
    try:
        
        if not inventario:
            raise ValueError("El inventario está completamente vacío. No se pueden calcular estadísticas.")

        productos_distintos = len({prod['nombre'] for prod in inventario if 'nombre' in prod})

        total_stock = sum(prod.get('stock', 0) for prod in inventario)

        total_precio = sum(prod.get('precio', 0.0) for prod in inventario)
        precio_promedio = total_precio / len(inventario)

        stock_mayor_a_5 = [prod['nombre'] for prod in inventario if prod.get('stock', 0) > 5]


        categorias_unicas = {prod['categoria'] for prod in inventario if 'categoria' in prod}

       return {
            "productos_distintos": productos_distintos,
            "total_stock": total_stock,
            "precio_promedio": round(precio_promedio, 2),
            "stock_mayor_a_5": stock_mayor_a_5,
            "categorias": categorias_unicas
        }

    except ValueError as e:
        # Manejo de la excepción interna de inventario vacío
        print(f"Error de validación: {e}")
        return None
    except KeyError as e:
        # Manejo por si algún producto no tiene las llaves esperadas
        print(f"Error de estructura: Al producto le falta el campo obligatorio {e}")
        return None
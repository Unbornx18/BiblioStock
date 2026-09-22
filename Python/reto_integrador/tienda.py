import json

def procesar_reto_ventas():
    ventas_por_vendedor = {}
    unidades_por_producto = {}
    total_general = 0

    # Parte 1/4: Lectura del archivo y apertura de alertas en modo append
    with open('D:/Python/reto_integrador/ventas.json', 'r', encoding='utf-8') as archivo_json, \
     open('D:/Python/reto_integrador/alertas_ventas.txt', 'a', encoding='utf-8') as archivo_alertas:
        
        ventas = json.load(archivo_json)
        
        for venta in ventas:
            # Calcular el monto total de la venta actual
            monto = venta['cantidad'] * venta['precio_unitario']
            total_general += monto
            
            # Generar alertas de ventas destacadas
            if monto > 700000:
                alerta = f"{venta['vendedor']} - {venta['tienda']} - {venta['producto']} - ${monto}\n"
                archivo_alertas.write(alerta)
                
            # Agrupar montos por vendedor 
            vendedor = venta['vendedor']
            if vendedor not in ventas_por_vendedor:
                ventas_por_vendedor[vendedor] = []
            ventas_por_vendedor[vendedor].append(monto)
            
            # Acumular unidades por producto
            producto = venta['producto']
            unidades_por_producto[producto] = unidades_por_producto.get(producto, 0) + venta['cantidad']

    #Parte 2: Cálculos estadísticos
    estadisticas = {}
    for vendedor, montos in ventas_por_vendedor.items():
        estadisticas[vendedor] = {
            'total': sum(montos),
            'promedio': sum(montos) / len(montos),
            'maximo': max(montos),
            'minimo': min(montos)
        }

    producto_estrella = max(unidades_por_producto, key=unidades_por_producto.get)
    producto_menos_vendido = min(unidades_por_producto, key=unidades_por_producto.get)
    promedio_general = total_general / len(ventas)

    #Parte 3: Ranking de vendedores
    ranking_vendedores = [(v, stats['total']) for v, stats in estadisticas.items()]
    ranking_vendedores.sort(key=lambda x: x[1], reverse=True)
    
  

    #Parte 4: Generación del reporte
    with open('resumen_ventas.txt', 'w', encoding='utf-8') as archivo_resumen:
        archivo_resumen.write("=== REPORTE DE CIERRE DE MES ===\n")
        archivo_resumen.write(f"Total general vendido: ${total_general:,.2f}\n")
        archivo_resumen.write(f"Promedio general por venta: ${promedio_general:,.2f}\n\n")
        
        archivo_resumen.write(f"Producto estrella: {producto_estrella} ({unidades_por_producto[producto_estrella]} uds)\n")
        archivo_resumen.write(f"Producto menos vendido: {producto_menos_vendido} ({unidades_por_producto[producto_menos_vendido]} uds)\n\n")
        
        archivo_resumen.write("========= RANKING DE VENDEDORES ========\n")
        for i, (v, total) in enumerate(ranking_vendedores, 1):
            stats = estadisticas[v]
            archivo_resumen.write(
                f"{i}. {v} | Total: ${stats['total']:,.2f} | "
                f"Promedio: ${stats['promedio']:,.2f} | "
                f"Máx: ${stats['maximo']:,.2f} | Mín: ${stats['minimo']:,.2f}\n"
            )

if __name__ == "__main__":
    procesar_reto_ventas()
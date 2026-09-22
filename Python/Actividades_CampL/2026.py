tarifas = {
    "moto": 1500,
    "carro": 3000,
    "bus": 5000
}

tipo_vehiculo = input("Ingrese el tipo de vehículo (Moto, Carro, Bus): ").strip().lower()

if tipo_vehiculo in tarifas:
    try:
        
        horas = float(input("Ingrese la cantidad de horas estacionado: "))
        
        total_pagar = tarifas[tipo_vehiculo] * horas
        
        print(f"\nEl valor total a pagar por {horas} horas de {tipo_vehiculo.capitalize()} es: ${total_pagar:,.0f}")
        
    except ValueError:
        print("\nError: Por favor ingrese un número válido para la cantidad de horas.")
else:
    
    print("\nError: No se reconoce ese tipo de vehículo. Opciones válidas: Moto, Carro, Bus.")
'''Registro de invitados a un evento

Estás organizando un evento y llevas el control de los correos electrónicos de las

personas registradas en un conjunto (set), para evitar registros duplicados.

Escribe un programa que agregue un nuevo correo al conjunto, verifique si un

correo ya está registrado antes de intentar agregarlo (avisando al usuario si

ya existe), muestre cuántos invitados únicos hay registrados hasta el momento,

y elimine el registro de alguien que canceló su asistencia usando discard (para

evitar un error si esa persona nunca se había registrado).'''

def gestionar_evento():
    
    invitados = set()
    
    while True:
        print("\n Registro de Invitados ")
        print("1. Registrar nuevo correo")
        print("2. Ver total de invitados únicos")
        print("3. Cancelar asistencia")
        print("4. Salir")
        
        opcion = input("Elige una opción (1-4): ")
        
        if opcion == '1':
            correo = input("Ingresa el correo a registrar: ").strip().lower()
            
            
            if correo in invitados:
                print(f"Aviso: El correo '{correo}' ya se encuentra registrado.")
            else:
                invitados.add(correo)
                print(f"Éxito: '{correo}' ha sido registrado correctamente.")
                
        elif opcion == '2':
            
            print(f"Invitados únicos hasta el momento: {len(invitados)}")
            
        elif opcion == '3':
            correo = input("Ingresa el correo de quien canceló: ").strip().lower()
            
            
            invitados.discard(correo)
            print(f"🗑️ Se ha procesado la cancelación para '{correo}'.")
            
        elif opcion == '4':
            print("Saliendo del sistema de registro...")
            break
            
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


if __name__ == "__main__":
    gestionar_evento()
# Diccionario para almacenar las reservas de zapatillas
reservas = {}

# numero maximo de pares que se pueden reservar en total
max_reservas = 20

# Funcion que muestra el menú principal en pantalla
def menu_reserva():
    print("\nTOTEM AUTOATENCIÓN RESERVA STRIKE")
    print("1.- Reservar zapatillas")
    print("2.- Buscar zapatillas reservadas")
    print("3.- Ver stock de reservas")
    print("4.- Salir")


# Funcion para realizar una reserva de zapatillas
def reservar_zapatillas():
    print("---- Reservar Zapatillas ----")
     # Verifica si ya se alcanzo el limite de reservas
    if sum(reservas.values()) >= max_reservas:
        print("Error, stock completo")
        return
    
    nombre = input("Nombre del comprador: ").strip()

    # Verifica si el nombre ya está registrado
    if nombre in reservas:
        print("Error nombre ya registrado en la reserva.")
        return
    
    clave = input("Digite la palabra secreta para confirmar la reserva: ")

    # Si la frase es incorrecta se cancela la reserva
    if clave != "EstoyEnListaDeReserva":
        print("Error: palabra clave incorrecta. Reserva no realizada.")
        return
    
    # si esta correcto se registra la reserva con 1 par de zapatillas
    reservas[nombre] = 1
    print(f"Reserva realizada exitosamente para {nombre}")

# Función para buscar una reserva existente por nombre
def buscar_reserva():
    print("---- Buscar Zapatillas Reservadas ----")

    nombre = input("Nombre del comprador a buscar: ").strip()

    # Verifica si el nombre existe en el diccionario de reservas
    if nombre in reservas:
        cantidad = reservas[nombre] # se Obtiene cuantos pares hay reservados

        tipo = "Vip" if cantidad == 2 else "estandar" # Determina si es VIP o estándar
        print(f"Reserva encontrada: {nombre} - {cantidad} par(es) ({tipo})")

        # Si el cliente tiene 1 par y hay stock da la opcion de actualizar a VIP
        if cantidad == 1 and len(reservas) < max_reservas:
            vip = input("¿Desea pagar adicional para VIP y reservar 2 pares? (s/n): ").lower()
            if vip == "s":
                reservas[nombre] = 2 # Se actualiza su reserva a 2 pares
                print(f"Reserva actualizada a VIP. Ahora {nombre} tiene 2 pares reservados.")
            else:
                print("Manteniendo reserva actual.")
        elif cantidad == 2:
            print("Ya tiene una reserva VIP.")
    else:
        print("No se encontró ninguna reserva con ese nombre.")

# Funcion para mostrar cuántos pares han sido reservados y cuántos quedan disponibles
def ver_stock():
    print("-- Ver Stock de Reservas --")
    total_pares = sum(reservas.values()) # Suma todos los pares reservados
    print(f"Pares reservados: {total_pares}")
    print(f"Pares disponibles: {max_reservas - total_pares}")

# funcion principal 
def main():
    while True:
        menu_reserva()
        try:
            opcion = input("Seleccione una opción (1-4): ")
            if opcion == "1":
                reservar_zapatillas()
            elif opcion == "2":
                buscar_reserva()
            elif opcion == "3":
                ver_stock()
            elif opcion == "4":
                print("Programa terminado...")
                break
            else:
                print("Debe ingresar una opción válida!!") # Opcion fuera del rango
        except ValueError:
            print("Debe ingresar una opción válida!!")# para cuando no se ocupa un numero

main()
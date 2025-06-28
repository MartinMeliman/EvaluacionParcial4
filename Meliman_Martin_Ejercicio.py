
reservas = {}

max_reservas = 20

def menu_reserva():
    print("\nTOTEM AUTOATENCIÓN RESERVA STRIKE")
    print("1.- Reservar zapatillas")
    print("2.- Buscar zapatillas reservadas")
    print("3.- Ver stock de reservas")
    print("4.- Salir")

    
def reservar_zapatillas():
    print("---- Reservar Zapatillas ----")
    if sum(reservas.values()) >= max_reservas:
        print("Error, stock completo")
        return
    
    nombre = input("Nombre del comprador: ").strip
    
    if nombre in reservas:
        print("Error nombre ya registrado en la reserva.")
        return
    
    clave = input("Digite la palabra secreta para confirmar la reserva: ")

    if clave != "EstoyEnListaDeReserva":
        print("Error: palabra clave incorrecta. Reserva no realizada.")
        return
    reservas[nombre] = 1
    print(f"Reserva realizada exitosamente para {nombre}")
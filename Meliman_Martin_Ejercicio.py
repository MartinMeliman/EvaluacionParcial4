
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
    
    nombre = input("Nombre del comprador: ").strip()
    
    if nombre in reservas:
        print("Error nombre ya registrado en la reserva.")
        return
    
    clave = input("Digite la palabra secreta para confirmar la reserva: ")

    if clave != "EstoyEnListaDeReserva":
        print("Error: palabra clave incorrecta. Reserva no realizada.")
        return
    reservas[nombre] = 1
    print(f"Reserva realizada exitosamente para {nombre}")

def buscar_reserva():
    print("---- Buscar Zapatillas Reservadas ----")

    nombre = input("Nombre del comprador a buscar: ").strip()

    if nombre in reservas:
        cantidad = reservas[nombre]
        tipo = "Vip" if cantidad == 2 else "estandar"
        print(f"Reserva encontrada: {nombre} - {cantidad} par(es) ({tipo})")

        if cantidad == 1 and len(reservas) < max_reservas:
            vip = input("¿Desea pagar adicional para VIP y reservar 2 pares? (s/n): ").lower()
            if vip == "s":
                reservas[nombre] = 2
                print(f"Reserva actualizada a VIP. Ahora {nombre} tiene 2 pares reservados.")
            else:
                print("Manteniendo reserva actual.")
        elif cantidad == 2:
            print("Ya tiene una reserva VIP.")
    else:
        print("No se encontró ninguna reserva con ese nombre.")

def ver_stock():
    print("-- Ver Stock de Reservas --")
    total_pares = sum(reservas.values())
    print(f"Pares reservados: {total_pares}")
    print(f"Pares disponibles: {max_reservas - total_pares}")

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
                print("Debe ingresar una opción válida!!")
        except ValueError:
            print("Debe ingresar una opción válida!!")

main()
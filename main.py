from menu.menu_inicio import mostrar_menu

def main():
    print("Bienvenido a JuegoTEC")
    eleccion = mostrar_menu()

    if eleccion == 'jugar':
        print("Aquí irá la lógica para iniciar el juego 3D")
        # Aquí podrías hacer: iniciar_juego()
    elif eleccion == 'creditos':
        print("Juego creado por el equipo de JuegoTEC")
    else:
        print("Opción no válida o se cerró el menú.")

if __name__ == '__main__':
    main()

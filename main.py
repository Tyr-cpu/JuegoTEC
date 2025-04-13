from menu.menu_inicio import mostrar_menu

def main():
    print("Bienvenido a JuegoTEC")
    eleccion = mostrar_menu()

    if eleccion == 'jugar':
        print("Aquí irá la lógica para iniciar el juego 3D")
        # Aquí se podría cargar el juego real, por ejemplo:
        # from juego.juego_principal import iniciar_juego
        # iniciar_juego()
    elif eleccion == 'creditos':
        print("Juego creado por el equipo de JuegoTEC")
        # Podrías mostrar una pantalla de créditos aquí si lo deseas
    else:
        print("El jugador cerró el menú o no eligió una opción válida.")

if __name__ == '__main__':
    main()

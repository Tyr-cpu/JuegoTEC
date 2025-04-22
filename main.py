from menu.menu_inicio import mostrar_menu
from menu.seleccion_personaje import mostrar_seleccion_personaje

def main():
    while True:
        eleccion = mostrar_menu()

        if eleccion == 'jugar':
            personaje = mostrar_seleccion_personaje()
            if personaje == 'menu':
                continue
            else:
                print(f"Personaje seleccionado: {personaje}")
                break  # Aquí puedes iniciar el juego principal
        elif eleccion == 'creditos':
            print("Juego creado por el equipo de JuegoTEC")
        else:
            print("Se cerró el juego.")
            break

if __name__ == '__main__':
    main()

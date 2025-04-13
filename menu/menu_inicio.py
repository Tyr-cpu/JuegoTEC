from ursina import *

def mostrar_menu():
    app = Ursina()
    opcion_elegida = None

    def jugar():
        nonlocal opcion_elegida
        opcion_elegida = 'jugar'
        destroy(menu_ui)
        app.userExit()

    def creditos():
        nonlocal opcion_elegida
        opcion_elegida = 'creditos'
        destroy(menu_ui)
        app.userExit()

    def salir():
        application.quit()

    # Fondo y botones
    menu_ui = Entity()

    fondo = Entity(model='quad', texture='white_cube', color=color.azure, scale=(16, 9), parent=menu_ui)

    Text("JuegoTEC", origin=(0,0), scale=2, y=0.4, parent=menu_ui)

    Button(text='Jugar', scale=(0.3,0.1), y=0.1, color=color.green, on_click=jugar, parent=menu_ui)
    Button(text='Créditos', scale=(0.3,0.1), y=-0.05, color=color.orange, on_click=creditos, parent=menu_ui)
    Button(text='Salir', scale=(0.3,0.1), y=-0.2, color=color.red, on_click=salir, parent=menu_ui)

    app.run()
    return opcion_elegida

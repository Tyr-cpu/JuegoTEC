from ursina import *

def mostrar_menu():
    app = Ursina()
    aspect_ratio = window.aspect_ratio
    opcion_elegida = None

    # Intentar cargar la textura
    ruta = 'assets/texturas/fondo_menu2.png'

    textura = load_texture(ruta)

    if not textura:
        print(f"❌ No se pudo cargar la textura: {ruta}")
    else:
        print(f"✅ Textura cargada correctamente: {ruta}")

    # Funciones de los botones
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

    # Crear menú
    menu_ui = Entity()

    # Fondo (si no se carga la imagen, usará un color por defecto)
    fondo = Entity(
        model='quad',
        texture=textura if textura else None,
        color=color.azure if not textura else color.white,
        scale=(aspect_ratio * 9, 9),
        parent=menu_ui
    )

    # Botones
    Button(text='Jugar', scale=(0.4, 0.1), y=0.2, on_click=jugar, parent=menu_ui)
    Button(text='Créditos', scale=(0.4, 0.1), y=0.0, on_click=creditos, parent=menu_ui)
    Button(text='Salir', scale=(0.4, 0.1), y=-0.2, on_click=salir, parent=menu_ui)

    # Ejecutar menú
    app.run()

    return opcion_elegida

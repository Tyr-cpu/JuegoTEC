from ursina import *

def mostrar_menu():
    app = Ursina()
    opcion_elegida = None

    # Imagen de fondo
    ruta = 'assets/texturas/fondo_menu2.png'
    textura = load_texture(ruta)
    if not textura:
        print("❌ No se cargó la textura del fondo.")
    else:
        print("✅ Fondo cargado correctamente.")

    # Fondo (pantalla completa)
    fondo = Entity(
        model='quad',
        texture=textura,
        scale=(16, 9),  # 16:9 para que se vea bien centrado
        parent=scene
    )

    # Funciones de botón
    def jugar():
        nonlocal opcion_elegida
        opcion_elegida = 'jugar'
        app.userExit()

    def creditos():
        nonlocal opcion_elegida
        opcion_elegida = 'creditos'
        app.userExit()

    def salir():
        application.quit()

    # Botones invisibles (alineados con los botones dibujados en la imagen)
    botones = []

    botones.append(Button(
        text='',
        color=color.clear,
        scale=(0.35, 0.10),
        position=(-0.501, -0.40),
        on_click=jugar
    ))

    botones.append(Button(
        text='',
        color=color.clear,
        scale=(0.35, 0.10),
        position=(0.00, -0.40),
        on_click=creditos
    ))

    botones.append(Button(
        text='',
        color=color.clear,
        scale=(0.35, 0.10),
        position=(0.505, -0.40),
        on_click=salir
    ))

    # Para ayudarte a ver dónde están, podés ponerle color temporal:
    # for b in botones: b.color = color.rgba(255,0,0,100)

    app.run()

    return opcion_elegida

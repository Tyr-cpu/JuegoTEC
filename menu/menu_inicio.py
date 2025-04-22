from ursina import *

def mostrar_menu():
    opcion_elegida = None

    def jugar():
        nonlocal opcion_elegida
        opcion_elegida = 'jugar'
        app.running = False

    def creditos():
        nonlocal opcion_elegida
        opcion_elegida = 'creditos'
        app.running = False

    def salir():
        application.quit()

    app = Ursina()

    # Fondo
    fondo = Entity(model='quad',
                   texture='assets/texturas/fondo_menu2.png',
                   scale=(16, 9))

    # Botones invisibles encima de la imagen
    botones = []
    botones.append(Button(text='', color=color.clear, scale=(0.35, 0.10),
                          position=(-0.501, -0.40), on_click=jugar))
    botones.append(Button(text='', color=color.clear, scale=(0.35, 0.10),
                          position=(0.00, -0.40), on_click=creditos))
    botones.append(Button(text='', color=color.clear, scale=(0.35, 0.10),
                          position=(0.505, -0.40), on_click=salir))
    
    # Mostrar los botones temporalmente en rojo semitransparente para ver su posición
    for b in botones:
        b.color = color.rgba(255, 0, 0, 100)


    app.run()
    return opcion_elegida

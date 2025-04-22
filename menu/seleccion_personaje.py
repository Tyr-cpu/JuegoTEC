from ursina import *

def mostrar_seleccion_personaje():
    personaje_elegido = None

    def seleccionar_personaje(numero):
        nonlocal personaje_elegido
        personaje_elegido = numero
        app.running = False

    def regresar():
        nonlocal personaje_elegido
        personaje_elegido = 'menu'
        app.running = False

    app = Ursina()

    fondo = Entity(model='quad',
                   texture='assets/texturas/fondo_seleccion_personaje.png',
                   scale=(16, 9))

    # Slots de personajes (ajusta las posiciones)
    botones_personaje = []
    posiciones = [-0.6, -0.2, 0.2, 0.6]
    for i, pos in enumerate(posiciones):
        botones_personaje.append(Button(text='', color=color.clear,
                                        scale=(0.25, 0.3),
                                        position=(pos, 0),
                                        on_click=lambda i=i: seleccionar_personaje(i)))

    # Botón de regreso
    boton_regresar = Button(text='', color=color.clear,
                            scale=(0.2, 0.08),
                            position=(-0.7, -0.4),
                            on_click=regresar)

    app.run()
    return personaje_elegido

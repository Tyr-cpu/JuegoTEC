# 🎮 JuegoTEC

JuegoTEC es un videojuego 3D ambientado en un laberinto dentro de un edificio escolar de 3 plantas. Fue desarrollado por un equipo de 5 personas como proyecto académico. El objetivo del juego es explorar el edificio, esquivar enemigos, recolectar llaves, abrir puertas y llegar al último piso para ganar. Está hecho con Python y **Ursina Engine**.

---

## 🚀 Características principales

- ✅ Menú principal con navegación completa (Inicio, Créditos, Salir)
- 🎭 Selección de personajes antes de comenzar a jugar
- 🔑 Cofres, llaves y puertas para progresar entre plantas
- 🧠 Enemigos con IA básica que patrullan o persiguen
- 🗺️ Mapas 3D representando los 3 pisos del edificio escolar
- 🧍 Jugador con animaciones y detección de colisiones
- 🎧 Sonido ambiental y efectos por evento (cofres, pasos, victoria, etc.)
- 🏆 Pantalla de victoria o derrota al finalizar el juego

---

## 🧩 Estructura del proyecto

```bash
JuegoTEC/
│
├── main.py                  # Punto de entrada del juego
├── menu/                   # Menús, selección de personaje, transiciones
├── entidades/              # Clases base de jugador y enemigos
├── personajes/             # Lógica y animaciones del jugador
├── enemigos/               # IA de enemigos y comportamiento
├── objetos/                # Cofres, llaves y puertas
├── logica/                 # Control del nivel, estado del juego
├── mapas/                  # Mapas 3D de cada planta del edificio
├── assets/
│   └── modelos/            # Modelos 3D importados (Blender, etc.)
├── sonido/                 # Música y efectos
├── README.md               # Este archivo
├── CONTRIB.md              # Guía para colaborar en equipo
```

## 👥 Equipo de desarrollo
Bryan – Menú y navegación + Integración general

Persona 2 – Jugador y entidades comunes

Persona 3 – Enemigos e inteligencia artificial

Persona 4 – Objetos y lógica del laberinto

Persona 5 – Modelado 3D, colisiones y sonido

## Cómo comenzar

### 1. Clonar el repositorio

```bash
git clone https://github.com/Tyr-cpu/JuegoTEC
cd laberinto3d
```

### 2. Instalar dependencias

Necesitas Python 3.8+ y Ursina:

```bash
pip install ursina
```

### 3. Ejecutar el juego

```bash
python main.py
```

## Trabajo en equipo - Buenas prácticas

- Siempre haz `git pull` antes de empezar.
- Usa `git add .`, `git commit -m "mensaje"` y `git push` para guardar tus avances.
- Usa ramas (`git checkout -b rama-nueva`) si trabajas en algo grande.
- Sé claro con tus mensajes de commit.
- No subas archivos pesados innecesarios (videos, renders, etc.).

## Créditos

Desarrollado por un equipo de 5 personas para un juego escolar en 3D.

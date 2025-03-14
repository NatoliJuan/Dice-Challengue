import streamlit as st
import random

# Título
st.title("🎲 Juego de Dados Interactivo")

# Paso 1: Seleccionar número de jugadores
num_jugadores = st.number_input("Número de jugadores:", min_value=1, max_value=6, step=1, value=2)

# Crear diccionario de jugadores
listado_jugadores = {f"JUGADOR {i+1}": [-1, -1, -1, -1, -1, -1] for i in range(num_jugadores)}

# Inicializar sesión
if "turno" not in st.session_state:
    st.session_state["turno"] = 0
if "jugador_actual" not in st.session_state:
    st.session_state["jugador_actual"] = list(listado_jugadores.keys())[0]
if "resultados" not in st.session_state:
    st.session_state["resultados"] = {j: [-1, -1, -1, -1, -1, -1] for j in listado_jugadores}

# Mostrar turno actual y jugador
st.write("### Turno actual:", st.session_state["turno"] + 1)
st.write("### Jugador actual:", st.session_state["jugador_actual"])

# Simular tirada de dados
if st.button("🎲 Lanzar Dados"):
    tirada = [random.randint(1, 6) for _ in range(5)]
    st.write("🎲 Dados obtenidos:", tirada)
    
    # Elegir cara
    eleccion_cara = st.selectbox("Elige una cara para puntuar:", [1, 2, 3, 4, 5, 6])
    caras_contadas = tirada.count(eleccion_cara)
    
    # Actualizar resultados
    jugador_actual = st.session_state["jugador_actual"]
    st.session_state["resultados"][jugador_actual][eleccion_cara - 1] = caras_contadas * eleccion_cara

    # Cambiar de jugador o de turno
    jugadores = list(listado_jugadores.keys())
    idx = jugadores.index(jugador_actual)
    
    if idx < len(jugadores) - 1:
        st.session_state["jugador_actual"] = jugadores[idx + 1]
    else:
        st.session_state["jugador_actual"] = jugadores[0]
        st.session_state["turno"] += 1

# Mostrar puntajes actuales
st.write("### Puntuaciones actuales:")
for jugador, puntuaciones in st.session_state["resultados"].items():
    st.write(f"{jugador}: {sum(puntuaciones)} puntos")

# Determinar ganador al final
if st.session_state["turno"] >= 6:
    total_puntos = {j: sum(p) for j, p in st.session_state["resultados"].items()}
    ganador = max(total_puntos, key=total_puntos.get)
    st.success(f"🎉 El ganador es {ganador} con {total_puntos[ganador]} puntos. ¡Felicidades!")

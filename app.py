import streamlit as st
import pandas as pd

# ---------------------------------------------------------
# CONFIGURACIÓN
# ---------------------------------------------------------
st.set_page_config(
    page_title="Karasuno — Explorador de Jugadores",
    page_icon="🏐",
    layout="wide",
)

# ---------------------------------------------------------
# ESTILO (mismo lenguaje visual que la página HTML)
# ---------------------------------------------------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Anton&family=Work+Sans:wght@400;500;600;700&display=swap');

    .stApp{ background:#14171c; color:#ced2da; font-family:'Work Sans', sans-serif; }
    h1, h2, h3{ font-family:'Anton', sans-serif !important; letter-spacing:0.5px; color:#fff !important; }

    .jersey-card{
        background:#1b1f27; border:1px solid #2b303b; border-left:5px solid #ff6a1a;
        padding:18px 20px; border-radius:6px; margin-bottom:14px;
    }
    .jersey-card .num{ font-family:'Anton', sans-serif; font-size:2.2rem; color:#ff6a1a; line-height:1; }
    .jersey-card .name{ font-size:1.1rem; font-weight:700; color:#fff; margin-top:4px; }
    .jersey-card .role{ color:#ffcd3c; font-size:0.8rem; font-weight:600; }

    [data-testid="stSidebar"]{ background:#1b1f27; }

    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# DATOS DE PERSONAJES
# ---------------------------------------------------------
jugadores = [
    {"num": 1, "nombre": "Sawamura Daichi", "posicion": "Ala-rematador (capitán)",
     "altura": 179, "salto": 78, "velocidad": 70, "tecnica": 84, "experiencia": 96,
     "frase": "Como capitán, confío en cada uno de mis compañeros."},
    {"num": 2, "nombre": "Sugawara Koushi", "posicion": "Colocador suplente",
     "altura": 174, "salto": 65, "velocidad": 60, "tecnica": 88, "experiencia": 95,
     "frase": "Un buen líder también sabe cuándo no jugar."},
    {"num": 3, "nombre": "Asahi Azumane", "posicion": "Ala-rematador (as)",
     "altura": 184, "salto": 88, "velocidad": 65, "tecnica": 85, "experiencia": 82,
     "frase": "Puedo con esto. Confío en mi equipo."},
    {"num": 4, "nombre": "Nishinoya Yuu", "posicion": "Líbero",
     "altura": 159, "salto": 70, "velocidad": 92, "tecnica": 90, "experiencia": 88,
     "frase": "Ninguna pelota toca el suelo mientras yo esté aquí."},
    {"num": 5, "nombre": "Tanaka Ryunosuke", "posicion": "Ala-rematador",
     "altura": 178, "salto": 85, "velocidad": 78, "tecnica": 70, "experiencia": 80,
     "frase": "¡Vamos con todo, Karasuno!"},
    {"num": 9, "nombre": "Kageyama Tobio", "posicion": "Colocador",
     "altura": 180, "salto": 80, "velocidad": 75, "tecnica": 98, "experiencia": 85,
     "frase": "Quiero ganar. Solo eso."},
    {"num": 10, "nombre": "Hinata Shoyo", "posicion": "Rematador de punta",
     "altura": 162, "salto": 97, "velocidad": 95, "tecnica": 60, "experiencia": 40,
     "frase": "¡Todavía puedo volar más alto!"},
    {"num": 12, "nombre": "Yamaguchi Tadashi", "posicion": "Ala-rematador (servicio)",
     "altura": 172, "salto": 68, "velocidad": 62, "tecnica": 72, "experiencia": 55,
     "frase": "Mi saque flotante puede cambiar el partido."},
]

df = pd.DataFrame(jugadores)

# Cuerpo técnico y manager — se muestran aparte, no tienen stats de juego
staff = [
    {"nombre": "Ukai Keishin", "rol": "Entrenador",
     "frase": "El talento sin ganas de mejorar no llega a ningún lado."},
    {"nombre": "Shimizu Kiyoko", "rol": "Manager",
     "frase": "Alguien tiene que llevar el orden mientras ustedes gritan."},
]

# ---------------------------------------------------------
# SIDEBAR — FILTROS
# ---------------------------------------------------------
st.sidebar.title("🏐 Filtros")

posiciones = ["Todas"] + sorted(df["posicion"].unique().tolist())
filtro_posicion = st.sidebar.selectbox("Posición", posiciones)

altura_min, altura_max = st.sidebar.slider(
    "Rango de altura (cm)", 150, 200, (150, 200)
)

busqueda = st.sidebar.text_input("Buscar por nombre")

df_filtrado = df.copy()
if filtro_posicion != "Todas":
    df_filtrado = df_filtrado[df_filtrado["posicion"] == filtro_posicion]
df_filtrado = df_filtrado[
    (df_filtrado["altura"] >= altura_min) & (df_filtrado["altura"] <= altura_max)
]
if busqueda:
    df_filtrado = df_filtrado[df_filtrado["nombre"].str.contains(busqueda, case=False)]

# ---------------------------------------------------------
# ENCABEZADO
# ---------------------------------------------------------
st.title("Explorador de Jugadores — Karasuno")
st.caption(f"Mostrando {len(df_filtrado)} de {len(df)} jugadores")

if df_filtrado.empty:
    st.warning("Ningún jugador coincide con esos filtros. Prueba ajustarlos.")
    st.stop()

# ---------------------------------------------------------
# LISTA + DETALLE
# ---------------------------------------------------------
col_lista, col_detalle = st.columns([1, 1.4])

with col_lista:
    nombre_seleccionado = st.radio(
        "Selecciona un jugador",
        df_filtrado["nombre"].tolist(),
        label_visibility="collapsed",
    )
    for _, j in df_filtrado.iterrows():
        st.markdown(
            f"""
            <div class="jersey-card">
                <div class="num">{j['num']}</div>
                <div class="name">{j['nombre']}</div>
                <div class="role">{j['posicion']}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

with col_detalle:
    jugador = df_filtrado[df_filtrado["nombre"] == nombre_seleccionado].iloc[0]

    st.subheader(f"#{jugador['num']} — {jugador['nombre']}")
    st.markdown(f"**Posición:** {jugador['posicion']}")
    st.markdown(f"**Altura:** {jugador['altura']} cm")
    st.markdown(f"> *\"{jugador['frase']}\"*")

    st.markdown("#### Estadísticas")
    stats = {
        "Salto": jugador["salto"],
        "Velocidad": jugador["velocidad"],
        "Técnica": jugador["tecnica"],
        "Experiencia": jugador["experiencia"],
    }
    for etiqueta, valor in stats.items():
        st.write(etiqueta)
        st.progress(valor / 100)

    st.markdown("#### Comparar con otro jugador")
    otro_nombre = st.selectbox(
        "Comparar contra",
        [n for n in df["nombre"] if n != nombre_seleccionado],
    )
    otro = df[df["nombre"] == otro_nombre].iloc[0]

    comparacion = pd.DataFrame(
        {
            jugador["nombre"]: [jugador["salto"], jugador["velocidad"], jugador["tecnica"], jugador["experiencia"]],
            otro["nombre"]: [otro["salto"], otro["velocidad"], otro["tecnica"], otro["experiencia"]],
        },
        index=["Salto", "Velocidad", "Técnica", "Experiencia"],
    )
    st.bar_chart(comparacion)

# ---------------------------------------------------------
# TABLA COMPLETA
# ---------------------------------------------------------
with st.expander("Ver tabla completa de jugadores filtrados"):
    st.dataframe(
        df_filtrado[["num", "nombre", "posicion", "altura", "salto", "velocidad", "tecnica", "experiencia"]],
        hide_index=True,
        use_container_width=True,
    )

# ---------------------------------------------------------
# CUERPO TÉCNICO
# ---------------------------------------------------------
st.markdown("---")
st.markdown("### Cuerpo técnico")

col_a, col_b = st.columns(2)
for col, persona in zip((col_a, col_b), staff):
    with col:
        st.markdown(
            f"""
            <div class="jersey-card" style="border-left-color:#ffcd3c;">
                <div class="role">{persona['rol']}</div>
                <div class="name">{persona['nombre']}</div>
                <p style="margin-top:8px; font-style:italic; color:#ced2da;">"{persona['frase']}"</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

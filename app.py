import streamlit as st

# ---------------------------------------------------------
# CONFIGURACIÓN DE PÁGINA
# ---------------------------------------------------------
st.set_page_config(
    page_title="Haikyuu!! — Karasuno vuela más alto",
    page_icon="🏐",
    layout="wide",
)

# ---------------------------------------------------------
# CSS PERSONALIZADO (misma dirección de diseño que la versión HTML)
# ---------------------------------------------------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Anton&family=Work+Sans:wght@400;500;600;700&display=swap');

    :root{
        --ink: #14171c;
        --court: #eee3c8;
        --court-line: #cabb95;
        --orange: #ff6a1a;
        --navy: #232a4d;
        --yellow: #ffcd3c;
        --ink-soft: #ced2da;
        --text-dark: #1c1f26;
    }

    /* Fondo general de la app */
    .stApp{
        background: var(--court);
        color: var(--text-dark);
        font-family: 'Work Sans', sans-serif;
    }

    /* Quita el padding gigante que Streamlit pone por defecto */
    .block-container{
        padding-top: 0rem;
        padding-bottom: 3rem;
        max-width: 100%;
    }

    .display{
        font-family: 'Anton', sans-serif;
        letter-spacing: 0.5px;
        line-height: 0.95;
    }

    /* ---------- HERO ---------- */
    .hero{
        position: relative;
        background: var(--ink);
        color: #fff;
        padding: 90px 6% 70px;
        margin: 0 -6rem 0 -6rem;
        clip-path: polygon(0 0, 100% 0, 100% 88%, 0 100%);
        overflow: hidden;
    }
    .hero::before{
        content:"";
        position:absolute;
        inset:0;
        background:
          linear-gradient(135deg, transparent 46%, rgba(255,106,26,0.9) 46%, rgba(255,106,26,0.9) 49%, transparent 49%),
          linear-gradient(135deg, transparent 51%, var(--navy) 51%);
        opacity:0.9;
    }
    .hero-inner{ position:relative; max-width:640px; }
    .hero .kicker{ font-weight:600; color:var(--yellow); font-size:1.05rem; margin-bottom:10px; }
    .hero h1{ font-size:clamp(2.6rem, 6vw, 4.8rem); color:#fff; margin:0; }
    .hero h1 .stroke{ -webkit-text-stroke: 2px var(--orange); color:transparent; }
    .hero p.lead{ margin-top:18px; max-width:38ch; font-size:1.1rem; color:var(--ink-soft); }

    .stats{ position:relative; display:flex; gap:40px; margin-top:40px; flex-wrap:wrap; }
    .stats .num{ font-family:'Anton', sans-serif; font-size:2.2rem; color:var(--orange); }
    .stats .label{ font-size:0.85rem; color:var(--ink-soft); }

    /* ---------- SECCIONES ---------- */
    .section-pad{ padding: 60px 6% 10px; }
    .section-head h2{ font-size: clamp(1.8rem, 3.4vw, 2.4rem); margin-bottom:6px; }
    .section-head p{ color:#4a4d55; max-width:60ch; }

    .card-quote{
        background: var(--navy);
        color: #fff;
        padding: 30px;
        border-left: 6px solid var(--orange);
        font-style: italic;
        border-radius: 4px;
    }
    .card-quote footer{
        margin-top:14px; font-size:0.85rem; color:var(--ink-soft); font-style:normal;
    }

    /* ---------- ROSTER (jerseys) ---------- */
    .roster-wrap{ background: var(--ink); color:#fff; margin: 40px -6rem 0 -6rem; padding: 60px 6%; }
    .roster-wrap .section-head p{ color: var(--ink-soft); }

    .jersey{
        background:#1b1f27;
        border:1px solid #2b303b;
        padding:22px 20px;
        border-radius: 6px;
        height: 100%;
        transition: border-color .2s ease, transform .2s ease;
    }
    .jersey:hover{ border-color: var(--orange); transform: translateY(-3px); }
    .jersey .number{ font-family:'Anton', sans-serif; font-size:2.6rem; color:var(--orange); line-height:1; }
    .jersey .name{ margin-top:6px; font-size:1.05rem; font-weight:700; }
    .jersey .role{ color: var(--yellow); font-weight:600; font-size:0.8rem; margin-top:2px; }
    .jersey .desc{ margin-top:10px; font-size:0.87rem; color: var(--ink-soft); }

    /* ---------- MARCADOR ---------- */
    .marcador-wrap{ background: var(--court-line); text-align:center; margin: 0 -6rem; padding: 60px 6%; }
    .board{
        background: var(--ink); color:#fff; max-width:760px; margin:0 auto;
        padding: 44px 36px; border: 3px solid var(--orange); border-radius: 6px;
    }
    .board .tag{ color: var(--yellow); font-weight:600; font-size:0.9rem; margin-bottom:14px; }
    .board .line{ font-family:'Anton', sans-serif; font-size:clamp(1.3rem, 3.2vw, 2.1rem); line-height:1.3; }
    .board .line .hi{ color: var(--orange); }

    footer.site{
        background: var(--navy); color: var(--ink-soft); padding: 24px 6%;
        margin: 0 -6rem -3rem -6rem; display:flex; justify-content:space-between;
        flex-wrap:wrap; gap:10px; font-size:0.85rem;
    }
    footer.site strong{ color:#fff; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# HERO
# ---------------------------------------------------------
st.markdown(
    """
    <div class="hero">
        <div class="hero-inner">
            <div class="kicker">Preparatoria Karasuno · Club de Vóleibol</div>
            <h1 class="display">VUELA<br><span class="stroke">MÁS ALTO</span></h1>
            <p class="lead">La cancha mide 9 metros de cada lado. Lo que ocurre dentro de ese cuadro,
            en Haikyuu!!, puede durar toda una vida.</p>
        </div>
        <div class="stats">
            <div><div class="num">4</div><div class="label">Temporadas</div></div>
            <div><div class="num">85</div><div class="label">Episodios</div></div>
            <div><div class="num">2014</div><div class="label">Año de estreno</div></div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# SINOPSIS
# ---------------------------------------------------------
st.markdown('<div class="section-pad">', unsafe_allow_html=True)
col1, col2 = st.columns([1.1, 0.9])
with col1:
    st.markdown(
        """
        <div class="section-head">
            <h2>Un rey sin trono, un cuervo sin vuelo</h2>
            <p>
            Shoyo Hinata quedó deslumbrado al ver un partido de vóleibol por televisión:
            un jugador bajito, apodado "el pequeño gigante", saltando por encima de
            rivales mucho más altos. Años después entra a Karasuno decidido a
            repetir esa hazaña, y ahí se cruza con Tobio Kageyama, un colocador
            brillante pero temido por su carácter.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
with col2:
    st.markdown(
        """
        <blockquote class="card-quote">
            <p>"No se trata de ganar solo el balón. Se trata de no dejar que la
            pelota toque el suelo, hasta el último segundo."</p>
            <footer>— Filosofía del equipo de Karasuno</footer>
        </blockquote>
        """,
        unsafe_allow_html=True,
    )
st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------------------------------
# ROSTER
# ---------------------------------------------------------
jugadores = [
    {"num": "10", "nombre": "Hinata Shoyo", "rol": "Rematador de punta",
     "desc": "Bajo estatura, salto descomunal. Compensa lo que le falta en altura con reflejos y velocidad."},
    {"num": "9", "nombre": "Kageyama Tobio", "rol": "Colocador",
     "desc": "Apodado 'el Rey de la cancha'. Lee el juego como nadie, aunque le costó aprender a confiar en su equipo."},
    {"num": "2", "nombre": "Sugawara Koushi", "rol": "Colocador suplente",
     "desc": "El corazón silencioso del equipo. Lidera desde la banca tanto como desde la cancha."},
    {"num": "5", "nombre": "Tanaka Ryunosuke", "rol": "Ala-rematador",
     "desc": "Puro fuego y ruido. Su remate de potencia intimida antes incluso de golpear el balón."},
    {"num": "4", "nombre": "Nishinoya Yuu", "rol": "Líbero",
     "desc": "El 'guardián supremo'. Ninguna pelota que él pueda alcanzar toca el suelo."},
    {"num": "11", "nombre": "Tsukishima Kei", "rol": "Central / bloqueador",
     "desc": "Frío, calculador, observador. Su bloqueo es una trampa que arma antes de que el rival lo note."},
]

st.markdown('<div class="roster-wrap">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="section-head">
        <h2>La alineación titular</h2>
        <p>Seis posiciones, seis formas distintas de entender el mismo deporte.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

cols = st.columns(3)
for i, jugador in enumerate(jugadores):
    with cols[i % 3]:
        st.markdown(
            f"""
            <div class="jersey">
                <div class="number">{jugador['num']}</div>
                <div class="name">{jugador['nombre']}</div>
                <div class="role">{jugador['rol']}</div>
                <p class="desc">{jugador['desc']}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------------------------------
# MARCADOR / FRASE FINAL
# ---------------------------------------------------------
st.markdown(
    """
    <div class="marcador-wrap">
        <div class="board">
            <div class="tag">Set final · punto de partido</div>
            <p class="line display">MIENTRAS LA PELOTA<br>NO TOQUE EL <span class="hi">SUELO</span>,<br>
            AÚN TENEMOS OPORTUNIDAD.</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------
st.markdown(
    """
    <footer class="site">
        <div><strong>Karasuno High</strong> · Club de Vóleibol</div>
        <div>Página de fans — Haikyuu!!</div>
    </footer>
    """,
    unsafe_allow_html=True,
)

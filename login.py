import streamlit as st

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
    }

    .login-box {
        background-color: rgba(255, 255, 255, 0.08);
        padding: 2rem;
        border-radius: 1rem;
        width: 100%;
        max-width: 400px;
        margin: auto;
        margin-top: 100px;
        box-shadow: 0 0 15px rgba(255, 255, 255, 0.2);
    }

    /* --- INPUTS: texto negro y fondo blanco translúcido --- */
    input, .stTextInput input {
        color: black !important;
        background-color: rgba(255, 255, 255, 0.9) !important;
        border: 1px solid rgba(0, 0, 0, 0.2);
        border-radius: 8px;
        padding: 0.5rem;
    }

    /* --- ETIQUETAS --- */
    label, .stTextInput label {
        color: white !important;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }

    /* --- BOTÓN --- */
    .stButton>button {
        background-color: #4CAF50;
        color: white !important;
        border: none;
        border-radius: 8px;
        padding: 0.6rem 1.2rem;
        font-weight: bold;
        margin-top: 1rem;
    }

    .stButton>button:hover {
        background-color: #45a049;
    }
    </style>
""", unsafe_allow_html=True)



# --- Diccionario de usuarios (usuario: contraseña) ---
USUARIOS = {
    "richi": "pandaking123",
    "ren": "superpanda"
}

# --- Login ---
def login():
    st.markdown('<div class="login-box">', unsafe_allow_html=True)
    
    st.markdown("### Inicia sesión")
    usuario = st.text_input("Usuario")
    contraseña = st.text_input("Contraseña", type="password")
    login_btn = st.button("Ingresar")

    if login_btn:
        if usuario in USUARIOS and USUARIOS[usuario] == contraseña:
            st.session_state["logueado"] = True
            st.session_state["usuario"] = usuario
            st.success(f"¡Bienvenido, {usuario}!")
        else:
            st.error("Usuario o contraseña incorrectos")
    
    st.markdown('</div>', unsafe_allow_html=True)

# --- App principal ---
def app_principal():
    st.title(f"Hola, {st.session_state['usuario']} 👋")
    st.write("Aquí va el contenido de tu app.")
    if st.button("Cerrar sesión"):
        st.session_state["logueado"] = False
        st.experimental_rerun()

# --- Control de sesión ---
if "logueado" not in st.session_state:
    st.session_state["logueado"] = False

if st.session_state["logueado"]:
    app_principal()
else:
    login()

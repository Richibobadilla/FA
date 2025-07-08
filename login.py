import streamlit as st

# --- CSS para fondo degradado y estilos bonitos ---
st.markdown("""
    <style>
    body {
        background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
    }
    .stApp {
        background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
        color: white;
    }
    .login-box {
        background-color: rgba(255, 255, 255, 0.1);
        padding: 2rem;
        border-radius: 1rem;
        width: 100%;
        max-width: 400px;
        margin: auto;
        margin-top: 100px;
        box-shadow: 0 0 20px rgba(255, 255, 255, 0.2);
    }
    input, button, label {
        color: white !important;
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
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Panda_icon.svg/2048px-Panda_icon.svg.png", width=100)  # Puedes reemplazar con tu logo
    st.title("Inicia sesión 🐼")

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
    st.write("Aquí puedes colocar el contenido principal de tu app del trabajo 📊📁")

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

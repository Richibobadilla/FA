import streamlit as st
from estilos import aplicar_estilos

aplicar_estilos()

# --- Diccionario de usuarios (usuario: contraseña) ---
USUARIOS = {
    "richi": "pandaking123",
    "ren": "superpanda"
}

# --- Login ---
def login():
    st.markdown('<div class="login-box">', unsafe_allow_html=True)
    
    st.markdown('<h1 style="color:white; text-align:center;">Inicia sesión</h1>', unsafe_allow_html=True)
    usuario = st.text_input("Usuario", key="usuario_login")
    contraseña = st.text_input("Contraseña", type="password", key="password_login")
    login_btn = st.button("Ingresar")

    if login_btn:
        if usuario in USUARIOS and USUARIOS[usuario] == contraseña:
            st.session_state["logueado"] = True
            st.session_state["usuario"] = usuario
            st.success(f"¡Bienvenido, {usuario}!")
            st.experimental_rerun()  # 🔁 Forzar recarga para entrar directo
        else:
            st.error("Usuario o contraseña incorrectos")

    st.markdown('</div>', unsafe_allow_html=True)

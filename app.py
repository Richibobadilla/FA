import streamlit as st
from login import login
from postlogin import postlogin
from estilos import aplicar_estilos

aplicar_estilos()  # 💅 Aplica tus colores y estilos

if "logueado" not in st.session_state:
    st.session_state["logueado"] = False

if not st.session_state["logueado"]:
    login()
else:
    postlogin()
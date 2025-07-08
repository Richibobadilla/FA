import streamlit as st
from login import login
from postlogin import postlogin

# Inicializa variable de sesión si no existe
if "logueado" not in st.session_state:
    st.session_state["logueado"] = False

# Si ya está logueado, mostrar post-login
if st.session_state["logueado"]:
    postlogin()
else:
    login()

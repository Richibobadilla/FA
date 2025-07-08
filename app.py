import streamlit as st
from login import login_view
from postlogin import post_login_view

# Control de sesión
if "logueado" not in st.session_state:
    st.session_state["logueado"] = False

# Flujo de la app
if st.session_state["logueado"]:
    post_login_view()
else:
    login_view()

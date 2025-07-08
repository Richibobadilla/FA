import streamlit as st
import pandas as pd
from estilos import aplicar_estilos

aplicar_estilos()  # 💅 Para conservar el diseño

def postlogin():
    st.title(f"Bienvenido, {st.session_state['usuario'].capitalize()} 👋")
    st.write("Puedes subir tu archivo Excel para comenzar:")

    archivo = st.file_uploader("Sube tu archivo Excel (.xlsx)", type=["xlsx"])

    if archivo:
        try:
            df = pd.read_excel(archivo)
            st.success("✅ Archivo cargado correctamente.")
            st.dataframe(df)
        except Exception as e:
            st.error(f"❌ Error al leer el archivo: {e}")

    # 👉 Espacio antes del botón
    st.markdown("<br><br>", unsafe_allow_html=True)

    # 👉 Botón rojo al fondo con clase personalizada
    st.markdown("""
        <style>
            .cerrar-btn > button {
                background-color: #f44336 !important;
                color: white !important;
                border: none;
                border-radius: 10px;
                padding: 0.6rem 1.2rem;
                font-weight: bold;
                margin-top: 2rem;
            }
        </style>
    """, unsafe_allow_html=True)

    with st.container():
        cerrar = st.button("🔒 Cerrar sesión", key="cerrar_btn", help="Haz clic para cerrar sesión.")
        if cerrar:
            st.session_state["logueado"] = False
            st.session_state["usuario"] = ""
            st.rerun()

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

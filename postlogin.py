import streamlit as st

def post_login_view():
    st.markdown(f"<h2 style='color: white;'>Bienvenido, {st.session_state['usuario']} 👋</h2>", unsafe_allow_html=True)
    st.write("Sube un archivo Excel para comenzar:")

    archivo = st.file_uploader("📂 Cargar archivo Excel", type=["xlsx"])

    if archivo:
        st.success("✅ Archivo recibido correctamente")
        # Aquí podrías leerlo con pandas:
        # import pandas as pd
        # df = pd.read_excel(archivo)
        # st.write(df)

    if st.button("Cerrar sesión"):
        st.session_state["logueado"] = False
        st.experimental_rerun()

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

    # 👉 Separador visual
    st.markdown("---")

    # 👉 Botón rojo de cerrar sesión al final
    cerrar = st.markdown("""
        <div style="display: flex; justify-content: center; margin-top: 30px;">
            <form action="" method="post">
                <button type="submit" style="
                    background-color: #f44336;
                    color: white;
                    border: none;
                    padding: 0.75rem 1.5rem;
                    font-size: 16px;
                    border-radius: 8px;
                    cursor: pointer;
                ">🔒 Cerrar sesión</button>
            </form>
        </div>
    """, unsafe_allow_html=True)

    # 👉 Capturar el evento con un workaround
    if "cerrar_sesion" not in st.session_state:
        st.session_state.cerrar_sesion = False

    if st.session_state.cerrar_sesion:
        st.session_state["logueado"] = False
        st.session_state["usuario"] = ""
        st.rerun()

    # ⚙️ Detectar click (truco con st.form solo si necesitas una acción directa)
    if st.button("🔒 Cerrar sesión", key="hidden_btn", help="Este botón es invisible", args=(), kwargs={}, disabled=True):
        st.session_state.cerrar_sesion = True

import streamlit as st

def aplicar_estilos():
    st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(to right, #c2e9fb, #a1c4fd);
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

        input, .stTextInput input {
            color: black !important;
            background-color: rgba(255, 255, 255, 0.9) !important;
            border: 1px solid rgba(0, 0, 0, 0.2);
            border-radius: 8px;
            padding: 0.5rem;
        }

        label, .stTextInput label {
            color: white !important;
            font-weight: 600;
        }

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

        div[data-testid="stNotificationContent"] * {
            opacity: 1 !important;
            color: white !important;
        }

        div[data-testid="stNotificationContent"]:not([role]) {
            background-color: #4CAF50 !important;
            border-radius: 8px !important;
            padding: 0.75rem 1rem !important;
        }

        div[data-testid="stNotificationContent"][role="alert"] {
            background-color: #f44336 !important;
            border-radius: 8px !important;
            padding: 0.75rem 1rem !important;
        }

        div[data-testid="stNotificationContent"][role="status"] {
            background-color: #ff9800 !important;
            color: black !important;
            border-radius: 8px !important;
            padding: 0.75rem 1rem !important;
        }
        
        /* 🔴 Botón rojo para cerrar sesión */
        div.stButton > button#cerrar_sesion {
            background-color: #f44336 !important;
            color: white !important;
        }
        </style>
    """, unsafe_allow_html=True)

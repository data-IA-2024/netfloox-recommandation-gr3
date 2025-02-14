from tabs.recommandation import Recommandation
from tabs.popularity import Popularity
from tabs.visualisation import Visualisation
from dotenv import load_dotenv
import os

import streamlit as st

load_dotenv()
USERS = {
    os.getenv("USER_1_EMAIL"): os.getenv("USER_1_PASSWORD"),
    os.getenv("USER_2_EMAIL"): os.getenv("USER_2_PASSWORD")
}

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    with st.container():
        st.title("🔐 Netfloox connection")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        if st.button("Connection", use_container_width=True):
            if email in USERS and USERS[email] == password:
                st.session_state["authenticated"] = True
                st.session_state["user"] = email
                st.success("Succesfull ! 🎉")
                st.rerun()
            else:
                st.error("incorrect ID or Password.")
    st.stop()

st.sidebar.image("assets/NETFLOOX.jpg", use_container_width=True)
st.sidebar.header(f"Welcome, {st.session_state['user']} !")
if st.sidebar.button("Disconnect", use_container_width=True):
    st.session_state["authenticated"] = False
    st.rerun()

selected_page = st.sidebar.radio("Navigation", ["Recommandation", "Popularity","Visualisation"], key="nav")

match selected_page:
    case "Recommandation":
        Recommandation()
    case "Popularity":
        Popularity()
    case "Visualisation":
        Visualisation()
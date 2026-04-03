import streamlit as st

st.set_page_config(page_title="Inventory Manager", layout="wide")

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if "username" not in st.session_state:
    st.session_state["username"] = ""

if "role" not in st.session_state:
    st.session_state["role"] = ""

st.title("Small Business Inventory Manager")

if st.session_state["logged_in"]:
    st.success(f"Logged in as {st.session_state['username']} ({st.session_state['role']})")
else:
    st.info("Please log in from the Login page.")
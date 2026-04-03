import streamlit as st

if not st.session_state.get("logged_in"):
    st.warning("Please log in first.")
    st.stop()

if st.session_state.get("role") != "admin":
    st.error("Access denied.")
    st.stop()

st.title("Admin Dashboard")
st.write(f"Welcome, {st.session_state['username']}!")


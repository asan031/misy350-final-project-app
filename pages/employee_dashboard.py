import streamlit as st

if not st.session_state.get("logged_in"):
    st.warning("Please log in first.")
    st.stop()

if st.session_state.get("role") != "employee":
    st.error("Access denied.")
    st.stop()

st.title("Employee Dashboard")
st.write(f"Welcome, {st.session_state['username']}!")

if st.button("Logout"):
    st.session_state["logged_in"] = False
    st.session_state["username"] = ""
    st.session_state["role"] = ""
    st.rerun()
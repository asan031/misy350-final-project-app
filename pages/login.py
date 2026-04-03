import streamlit as st
from utils.auth import login_user

st.title("Login")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if username == "" or password == "":
        st.error("Please fill in all fields.")
    else:
        user = login_user(username, password)

        if user:
            st.session_state["logged_in"] = True
            st.session_state["username"] = user["username"]
            st.session_state["role"] = user["role"]

            st.success("Login successful!")

            if user["role"] == "admin":
                st.switch_page("pages/admin_dashboard.py")
            elif user["role"] == "employee":
                st.switch_page("pages/employee_dashboard.py")
        else:
            st.error("Invalid username or password.")
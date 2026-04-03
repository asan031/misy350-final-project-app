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
            st.success("Login successful!")
        else:
            st.error("Invalid username or password.")
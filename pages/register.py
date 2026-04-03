import json
from pathlib import Path

import streamlit as st


# ---------- File path ----------
BASE_DIR = Path(__file__).resolve().parent.parent
USERS_FILE = BASE_DIR / "data" / "users.json"


# ---------- Helpers ----------
def load_users():
    if not USERS_FILE.exists():
        return []

    try:
        with open(USERS_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_users(users):
    with open(USERS_FILE, "w", encoding="utf-8") as file:
        json.dump(users, file, indent=4)


def username_exists(users, username):
    for user in users:
        if user["username"].lower() == username.lower():
            return True
    return False


def next_user_id(users):
    if not users:
        return 1
    return max(user["id"] for user in users) + 1


# ---------- Page UI ----------
st.title("Register")
st.write("Create an account to use the app.")

username = st.text_input("Username")
password = st.text_input("Password", type="password")
role = st.selectbox("Role", ["attendee", "admin"])

if st.button("Create Account"):
    users = load_users()

    username = username.strip()
    password = password.strip()

    if username == "":
        st.error("Username cannot be empty.")
    elif password == "":
        st.error("Password cannot be empty.")
    elif username_exists(users, username):
        st.error("That username already exists. Please choose another one.")
    else:
        new_user = {
            "id": next_user_id(users),
            "username": username,
            "password": password,
            "role": role
        }

        users.append(new_user)
        save_users(users)

        st.success("Account created successfully!")
        st.write("You can now go to the login page.")
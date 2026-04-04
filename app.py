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

    if st.button("Logout"):
        st.session_state["logged_in"] = False
        st.session_state["username"] = ""
        st.session_state["role"] = ""
        st.rerun()
else:
    st.info("Please log in from the Login page.")

# Admin Dashboard
import streamlit as st

if not st.session_state.get("logged_in"):
    st.warning("Please log in first.")
    st.stop()

if st.session_state.get("role") != "admin":
    st.error("Access denied.")
    st.stop()

st.title("Admin Dashboard")
st.write(f"Welcome, {st.session_state['username']}!")

if st.button("Logout"):
    st.session_state["logged_in"] = False
    st.session_state["username"] = ""
    st.session_state["role"] = ""
    st.rerun()

# Employee Dashboard
import streamlit as st
from utils.inventory_helpers import get_inventory

if not st.session_state.get("logged_in"):
    st.warning("Please log in first.")
    st.stop()

if st.session_state.get("role") != "employee":
    st.error("Access denied.")
    st.stop()

st.title("Employee Dashboard")
st.write(f"Welcome, {st.session_state['username']}!")

items = get_inventory()

st.subheader("Inventory Overview")

if not items:
    st.info("No inventory items found.")
else:
    for item in items:
        st.write(f"{item['name']} | Price: ${item['price']} | Stock: {item['stock']}")

low_stock_items = [item for item in items if item["stock"] <= 5]

st.subheader("Low Stock Alerts")

if not low_stock_items:
    st.success("No low-stock items right now.")
else:
    for item in low_stock_items:
        st.warning(f"{item['name']} is low on stock ({item['stock']} left)")

if st.button("Logout"):
    st.session_state["logged_in"] = False
    st.session_state["username"] = ""
    st.session_state["role"] = ""
    st.rerun()

#Login Page
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

#Manage Inventory

import streamlit as st
from utils.inventory_helpers import get_inventory, add_item, update_item, delete_item

if not st.session_state.get("logged_in"):
    st.warning("Please log in first.")
    st.stop()

if st.session_state.get("role") != "admin":
    st.error("Access denied.")
    st.stop()

st.title("Manage Inventory")


st.subheader("Add New Item")

name = st.text_input("Item Name")
price = st.number_input("Price", min_value=0.0, step=0.01)
stock = st.number_input("Stock", min_value=0, step=1)

if st.button("Add Item"):
    if name.strip() == "":
        st.error("Item name cannot be empty.")
    else:
        add_item(name.strip(), price, stock)
        st.success("Item added successfully!")
        st.rerun()


st.subheader("Current Inventory")

items = get_inventory()

if not items:
    st.info("No inventory items yet.")
else:
    for item in items:
        st.write(f"ID: {item['id']} | {item['name']} | ${item['price']} | Stock: {item['stock']}")


st.subheader("Update Item")

if items:
    item_options = {
        f"{item['id']} - {item['name']}": item["id"]
        for item in items
    }

    selected_label = st.selectbox("Select item to update", list(item_options.keys()))
    selected_item_id = item_options[selected_label]

    selected_item = None
    for item in items:
        if item["id"] == selected_item_id:
            selected_item = item
            break

    updated_name = st.text_input("New Item Name", value=selected_item["name"])
    updated_price = st.number_input("New Price", min_value=0.0, step=0.01, value=float(selected_item["price"]))
    updated_stock = st.number_input("New Stock", min_value=0, step=1, value=int(selected_item["stock"]))

    if st.button("Update Item"):
        if updated_name.strip() == "":
            st.error("Item name cannot be empty.")
        else:
            update_item(selected_item_id, updated_name.strip(), updated_price, updated_stock)
            st.success("Item updated successfully!")
            st.rerun()


st.subheader("Delete Item")

if items:
    for item in items:
        if st.button(f"Delete Item {item['id']}", key=f"delete_{item['id']}"):
            delete_item(item["id"])
            st.warning("Item deleted.")
            st.rerun()

#Record Sales

import streamlit as st
from utils.inventory_helpers import get_inventory, record_sale

if not st.session_state.get("logged_in"):
    st.warning("Please log in first.")
    st.stop()

if st.session_state.get("role") != "employee":
    st.error("Access denied.")
    st.stop()

st.title("Record Sales")

items = get_inventory()

if not items:
    st.info("No inventory items available.")
    st.stop()

st.subheader("Current Inventory")

available_items = []
for item in items:
    st.write(f"ID: {item['id']} | {item['name']} | ${item['price']} | Stock: {item['stock']}")
    if item["stock"] > 0:
        available_items.append(item)

if not available_items:
    st.warning("All items are out of stock.")
    st.stop()

st.subheader("Record a Sale")

item_options = {
    f"{item['id']} - {item['name']} (Stock: {item['stock']})": item["id"]
    for item in available_items
}

selected_label = st.selectbox("Choose an item", list(item_options.keys()))
selected_item_id = item_options[selected_label]

quantity = st.number_input("Quantity Sold", min_value=1, step=1)

if st.button("Record Sale"):
    success, message = record_sale(
        selected_item_id,
        quantity,
        st.session_state["username"]
    )

    if success:
        st.success(message)
        st.rerun()
    else:
        st.error(message)

#Register Page

import json
from pathlib import Path

import streamlit as st

BASE_DIR = Path(__file__).resolve().parent.parent
USERS_FILE = BASE_DIR / "data" / "users.json"

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
        if user.get("username", "").lower() == username.lower():
            return True
    return False


def next_user_id(users):
    if not users:
        return 1

    existing_ids = [user.get("id", 0) for user in users]
    return max(existing_ids) + 1


st.title("Register")
st.write("Create an account to use the app.")

username = st.text_input("Username")
password = st.text_input("Password", type="password")
role = st.selectbox("Role", ["employee", "admin"])

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

#Auth.py
import os
import json

USERS_FILE = "data/users.json"


def load_users():
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, "w") as file:
            json.dump([], file)

    with open(USERS_FILE, "r") as file:
        return json.load(file)


def login_user(username, password):
    users = load_users()

    for user in users:
        if user["username"] == username and user["password"] == password:
            return user

    return None

#Inventory Helpers
from utils.storage import load_data, save_data

INVENTORY_FILE = "data/inventory.json"
SALES_FILE = "data/sales.json"


def get_inventory():
    return load_data(INVENTORY_FILE)


def get_sales():
    return load_data(SALES_FILE)


def next_item_id(items):
    if not items:
        return 1
    return max(item.get("id", 0) for item in items) + 1


def next_sale_id(sales):
    if not sales:
        return 1
    return max(sale.get("id", 0) for sale in sales) + 1


def add_item(name, price, stock):
    items = get_inventory()

    new_item = {
        "id": next_item_id(items),
        "name": name,
        "price": price,
        "stock": stock
    }

    items.append(new_item)
    save_data(INVENTORY_FILE, items)


def update_item(item_id, new_name, new_price, new_stock):
    items = get_inventory()

    for item in items:
        if item["id"] == item_id:
            item["name"] = new_name
            item["price"] = new_price
            item["stock"] = new_stock
            break

    save_data(INVENTORY_FILE, items)


def delete_item(item_id):
    items = get_inventory()
    updated_items = [item for item in items if item["id"] != item_id]
    save_data(INVENTORY_FILE, updated_items)


def record_sale(item_id, quantity, employee_username):
    items = get_inventory()
    sales = get_sales()

    for item in items:
        if item["id"] == item_id:
            if quantity > item["stock"]:
                return False, "Not enough stock available."

            item["stock"] -= quantity

            sale = {
                "id": next_sale_id(sales),
                "item_id": item_id,
                "item_name": item["name"],
                "quantity": quantity,
                "employee": employee_username
            }

            sales.append(sale)

            save_data(INVENTORY_FILE, items)
            save_data(SALES_FILE, sales)

            return True, "Sale recorded successfully."

    return False, "Item not found."

#Storage.py
import json
import os


def load_data(file_path):
    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump([], f)
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read().strip()

            if content == "":
                return []

            return json.loads(content)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_data(file_path, data):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
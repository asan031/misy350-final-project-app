import streamlit as st
import json
import os
from pathlib import Path


#App Header and Status

st.set_page_config(page_title="Inventory Manager", layout="wide")

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if "username" not in st.session_state:
    st.session_state["username"] = ""

if "role" not in st.session_state:
    st.session_state["role"] = ""

if "page" not in st.session_state:
    st.session_state["page"] = "login"

st.title("Small Business Inventory Manager")

if st.session_state["logged_in"]:
    st.success(f"Logged in as {st.session_state['username']} ({st.session_state['role']})")
else:
    st.info("Please log in from the Login page.")

#Side Bar Navigation 
with st.sidebar:
    st.title("Inventory Manager")

    if st.session_state["logged_in"]:
        if st.button("Admin Dashboard", use_container_width=True):
            st.session_state["page"] = "admin_dashboard"
            st.rerun()

        if st.button("Employee Dashboard", use_container_width=True):
            st.session_state["page"] = "employee_dashboard"
            st.rerun()

        if st.button("Manage Inventory", use_container_width=True):
            st.session_state["page"] = "manage_inventory"
            st.rerun()

        if st.button("Record Sales", use_container_width=True):
            st.session_state["page"] = "record_sales"
            st.rerun()

        if st.button("Logout", use_container_width=True):
            st.session_state["logged_in"] = False
            st.session_state["username"] = ""
            st.session_state["role"] = ""
            st.session_state["page"] = "login"
            st.rerun()
    else:
        if st.button("Login", use_container_width=True):
            st.session_state["page"] = "login"
            st.rerun()

        if st.button("Register", use_container_width=True):
            st.session_state["page"] = "register"
            st.rerun()

#Storage Functions

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

#Authentication Functions

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

#Inventory Functions

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



#Login Page

if st.session_state["page"] == "login":
    st.header("Login")

    username = st.text_input("Username", key="login_username")
    password = st.text_input("Password", type="password", key="login_password")

    if st.button("Login", key="login_submit_btn"):
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
                    st.session_state["page"] = "admin_dashboard"
                elif user["role"] == "employee":
                    st.session_state["page"] = "employee_dashboard"

                st.rerun()
            else:
                st.error("Invalid username or password.")
    


#Register Page

elif st.session_state["page"] == "register":
    st.header("Register")
    st.write("Create an account to use the app.")

    username = st.text_input("Username", key="register_username")
    password = st.text_input("Password", type="password", key="register_password")
    role = st.selectbox("Role", ["employee", "admin"], key="register_role")

    if st.button("Create Account", key="register_submit_btn"):
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
            save_data(USERS_FILE, users)

            st.success("Account created successfully!")
            st.write("You can now go to the login page.")

# Admin Dashboard

elif st.session_state["page"] == "admin_dashboard":
    if not st.session_state.get("logged_in"):
        st.warning("Please log in first.")
        st.stop()

    if st.session_state.get("role") != "admin":
        st.error("Access denied.")
        st.stop()

    st.header("Admin Dashboard")
    st.write(f"Welcome, {st.session_state['username']}!")

# Employee Dashboard
elif st.session_state["page"] == "employee_dashboard":
    if not st.session_state.get("logged_in"):
        st.warning("Please log in first.")
        st.stop()

    if st.session_state.get("role") != "employee":
        st.error("Access denied.")
        st.stop()

    st.header("Employee Dashboard")
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



#Manage Inventory

elif st.session_state["page"] == "manage_inventory":
    if not st.session_state.get("logged_in"):
        st.warning("Please log in first.")
        st.stop()

    if st.session_state.get("role") != "admin":
        st.error("Access denied.")
        st.stop()

    st.header("Manage Inventory")

    st.subheader("Add New Item")

    name = st.text_input("Item Name", key="add_item_name")
    price = st.number_input("Price", min_value=0.0, step=0.01, key="add_item_price")
    stock = st.number_input("Stock", min_value=0, step=1, key="add_item_stock")

    if st.button("Add Item", key="add_item_btn"):
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

        selected_label = st.selectbox("Select item to update", list(item_options.keys()), key="update_item_select")
        selected_item_id = item_options[selected_label]

        selected_item = None
        for item in items:
            if item["id"] == selected_item_id:
                selected_item = item
                break

        updated_name = st.text_input("New Item Name", value=selected_item["name"], key="updated_name_input")
        updated_price = st.number_input("New Price", min_value=0.0, step=0.01, value=float(selected_item["price"]), key="updated_price_input")
        updated_stock = st.number_input("New Stock", min_value=0, step=1, value=int(selected_item["stock"]), key="updated_stock_input")

        if st.button("Update Item", key="update_item_btn"):
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

elif st.session_state["page"] == "record_sales":
    if not st.session_state.get("logged_in"):
        st.warning("Please log in first.")
        st.stop()

    if st.session_state.get("role") != "employee":
        st.error("Access denied.")
        st.stop()

    st.header("Record Sales")

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

    selected_label = st.selectbox("Choose an item", list(item_options.keys()), key="record_sale_select")
    selected_item_id = item_options[selected_label]

    quantity = st.number_input("Quantity Sold", min_value=1, step=1, key="record_sale_quantity")

    if st.button("Record Sale", key="record_sale_btn"):
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

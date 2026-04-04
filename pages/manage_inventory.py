import streamlit as st
from utils.inventory_helpers import get_inventory, add_item, update_item, delete_item

if not st.session_state.get("logged_in"):
    st.warning("Please log in first.")
    st.stop()

if st.session_state.get("role") != "admin":
    st.error("Access denied.")
    st.stop()

st.title("Manage Inventory")

# ---------- Add Item ----------
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

# ---------- Current Inventory ----------
st.subheader("Current Inventory")

items = get_inventory()

if not items:
    st.info("No inventory items yet.")
else:
    for item in items:
        st.write(f"ID: {item['id']} | {item['name']} | ${item['price']} | Stock: {item['stock']}")

# ---------- Update Item ----------
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

# ---------- Delete Item ----------
st.subheader("Delete Item")

if items:
    for item in items:
        if st.button(f"Delete Item {item['id']}", key=f"delete_{item['id']}"):
            delete_item(item["id"])
            st.warning("Item deleted.")
            st.rerun()
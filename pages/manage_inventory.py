import streamlit as st
from utils.inventory_helpers import get_inventory, add_item, delete_item

# ---------- Access Control ----------
if not st.session_state.get("logged_in"):
    st.warning("Please log in first.")
    st.stop()

if st.session_state.get("role") != "admin":
    st.error("Access denied.")
    st.stop()

# ---------- Page UI ----------
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

# ---------- View Inventory ----------
st.subheader("Current Inventory")

items = get_inventory()

if not items:
    st.info("No inventory items yet.")
else:
    for item in items:
        st.write(f"ID: {item['id']} | {item['name']} | ${item['price']} | Stock: {item['stock']}")

        if st.button(f"Delete Item {item['id']}", key=f"delete_{item['id']}"):
            delete_item(item["id"])
            st.warning("Item deleted.")
            st.rerun()
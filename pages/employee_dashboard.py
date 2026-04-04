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
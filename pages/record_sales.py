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
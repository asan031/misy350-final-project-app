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
from utils.data_manager import DataManager, INVENTORY_FILE, SALES_FILE


def get_inventory():
    return DataManager.load_json(INVENTORY_FILE)


def get_sales():
    return DataManager.load_json(SALES_FILE)


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

    for item in items:
        if item["name"].lower() == name.lower():
            item["stock"] += stock
            item["price"] = price
            DataManager.save_json(INVENTORY_FILE, items)
            return

    new_item = {
        "id": next_item_id(items),
        "name": name,
        "price": price,
        "stock": stock
    }

    items.append(new_item)
    DataManager.save_json(INVENTORY_FILE, items)


def update_item(item_id, new_name, new_price, new_stock):
    items = get_inventory()

    for item in items:
        if item["id"] == item_id:
            item["name"] = new_name
            item["price"] = new_price
            item["stock"] = new_stock
            break

    DataManager.save_json(INVENTORY_FILE, items)


def delete_item(item_id):
    items = get_inventory()
    updated_items = [item for item in items if item["id"] != item_id]
    DataManager.save_json(INVENTORY_FILE, updated_items)


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

            DataManager.save_json(INVENTORY_FILE, items)
            DataManager.save_json(SALES_FILE, sales)

            return True, "Sale recorded successfully."

    return False, "Item not found."
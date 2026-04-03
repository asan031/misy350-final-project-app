from utils.storage import load_data, save_data

INVENTORY_FILE = "data/inventory.json"


def get_inventory():
    return load_data(INVENTORY_FILE)


def next_item_id(items):
    if not items:
        return 1
    return max(item.get("id", 0) for item in items) + 1


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


def delete_item(item_id):
    items = get_inventory()
    updated_items = [item for item in items if item["id"] != item_id]
    save_data(INVENTORY_FILE, updated_items)
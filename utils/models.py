class User:
    def __init__(self, user_id, username, password, role):
        self.id = user_id
        self.username = username
        self.password = password
        self.role = role


class InventoryItem:
    def __init__(self, item_id, name, quantity, price):
        self.id = item_id
        self.name = name
        self.quantity = quantity
        self.price = price


class Sale:
    def __init__(self, sale_id, item_name, quantity_sold, total_price):
        self.id = sale_id
        self.item_name = item_name
        self.quantity_sold = quantity_sold
        self.total_price = total_price
from helpers.add import add


class Customer:
    def __init__(self):
        self.all_orders = 0

    def add_orders(self, new_orders: int):
        self.all_orders = add(self.all_orders, new_orders)

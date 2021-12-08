from main import Customer


class TestCustomer:
    def test_add_orders_1(self):
        customer = Customer()

        customer.add_orders(4)

        assert customer.all_orders == 4

    def test_add_orders_2(self):
        customer = Customer()

        customer.add_orders(5)
        customer.add_orders(3)

        assert customer.all_orders == 8

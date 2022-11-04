import csv


class Item:
    # class attribute
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Run validation to the received arguements
        assert price >= 0, f"Price {self.price} is should be greater or equal to zero"
        assert quantity >= 0, f"Quantity  {quantity} should be geater or equal to zero"

        # assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # appending the instance  each time an new instance is created
        Item.all.append(self)

    def total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as file:
            reader = csv.DictReader(file)
            items = list(reader)
        for item in items:
            Item(name=item.get('name'), price=float(item.get(
                'price')), quantity=float(item.get('quantity')))

    @staticmethod
    def is_integer(num):
        # counting out thr floates that are point zero. for i.e 5.0,10.0
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f" Item {self.name}, {self.price},{self.quantity}"


print(Item.is_integer(10.0))

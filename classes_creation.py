class Item:
    # class attribute
    pay_rate = 0.8

    def __init__(self, name: str, price: float, quantity=0):
        # Run validation to the received arguements
        assert price >= 0, f"Price {self.price} is should be greater or equal to zero"
        assert quantity >= 0, f"Quantity  {quantity} should be geater or equal to zero"
        # assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate


item_one = Item('phone', 100, 5)
print(item_one.total_price())
item_one.pay_rate = 0.7
item_one.apply_discount()
print(item_one.price)
# The __dict__ magic method
print(Item.__dict__)  # class level attributes
print("---------------------")
print(item_one.__dict__)  # object level attributes
print("---------------------")

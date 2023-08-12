class Item:
    pay_rate = 0.8  # The pay rate after 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments

        assert price > 0, f"Price greater than 0 expected, got: {price}"
        assert quantity > 0, f"Quantity greater than 0 expected, got: {quantity}"

        # Assign to self object
        self.__name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    @property
    # Property Decorator = Read-Only Attribute
    def name(self):
        return f"My name is: {self.__name}"

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long!")
        else:
            self.__name = value

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open("items.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get("name"),
                price=float(item.get("price")),
                quantity=int(item.get("quantity")),
            )

    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"Item('{self.__name}', {self.price}, {self.quantity})"


class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # Call to super function to have access to all attributes / methods
        super().__init__(name, price, quantity)

        # Run validations to the received arguments
        assert (
            broken_phones > 0
        ), f"Broken Phones {broken_phones} is expected greater than zero!"

        # Assign to self object
        self.broken_phones = broken_phones


phone1 = Phone("jscPhonev10", 500, 5, 1)

item = Item("Hat", 10, 2)

print(Item.all)
print(item.name)

# classmethod vs staticmethod
# classmethod: cls
# staticmethod: no self or cls

# A class method is a method that’s shared among all objects. Class methods can be can be called from instances and from the class itself

# Like a static method, a class method doesn’t need an object to be instantiated.

# A class method differs from a static method in that a static method doesn’t know about the class itself. In a classmethod, the parameter is always the class itself.

# a static method knows nothing about the class or instance. You can just as well use a function call.

# a class method gets the class when the method is called. It knows abouts the classes attributes and methods.

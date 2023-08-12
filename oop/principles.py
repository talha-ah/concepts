import csv


class Item:
    pay_rate = 0.8  # The pay rate after 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        # Assign to self object
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value

    @property
    def name(self):
        # Property Decorator = Read-Only Attribute
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long!")
        else:
            self.__name = value

    def calculate_total_price(self):
        return self.__price * self.quantity

    # private method
    def __connect(self, url):
        return "Connecting to smtp server..."

    # private method
    def __format_message(self):
        return f"""
        Hello Someone
        We have {self.name} {self.quantity} times.
        Regards, Abstraction
        """

    # private method
    def __send(self):
        return "Sending email..."

    def send_email(self):
        print("Starting sending email...")
        self.__connect("")
        self.__format_message()
        self.__send()

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
        return (
            f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})"
        )


item1 = Item("jscKeyboard", 750, 3)

# Encapsulation - data and methods hidden from the outside world - private methods/attributes
# some helper methods/attributes are private and can be accessed only from inside the class itself and provide some handlers/methods to the outside world like getters/setters
item1.apply_discount()
item1.apply_increment(0.2)

# Abstration - Unnecessary information hidden in the class (a method to hide the unnecassary/unwanted information)
# how something works is hidden from the outside world
item1.send_email()
# item1.__connect()  # Unable to access as this information is hidden

# Inheritance
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


# Polymorphism - Many forms
name = "Jim"  # str
print(len(name))

some_list = ["some", "name"]  # list
print(len(some_list))
# That's polymorphism in action, a single function does now
# how to handle different kinds of objects as expected!

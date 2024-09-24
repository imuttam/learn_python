"""The Product class is specified. An instance of this class named product was created.
Display the namespace (value of the __dict__ attribute) of this instance as shown below."""

import uuid


class Product:

    def __init__(self, product_name, product_id, price):
        self.product_name = product_name
        self.product_id = product_id
        self.price = price

    def __repr__(self):
        return (
            f"Product(product_name='{self.product_name}', ")

product = Product('Mobile Phone', '54274', 2900)
print(product.__dict__)
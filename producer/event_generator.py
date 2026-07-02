import random
from datetime import datetime
from faker import Faker

from schema import OrderEvent

fake = Faker("en_IN")

PRODUCTS = [
    ("PRD001", "Laptop", "Electronics", 65000),
    ("PRD002", "Keyboard", "Electronics", 1200),
    ("PRD003", "Office Chair", "Furniture", 8500),
    ("PRD004", "Running Shoes", "Fashion", 3500),
    ("PRD005", "Coffee Mug", "Home", 450)
]

PAYMENTS = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Net Banking",
    "Cash on Delivery"
]


def generate_order():

    product = random.choice(PRODUCTS)

    return OrderEvent(
        order_id=f"ORD{random.randint(100000,999999)}",
        customer_id=f"CUS{random.randint(1000,9999)}",
        customer_name=fake.name(),
        product_id=product[0],
        product_name=product[1],
        category=product[2],
        quantity=random.randint(1,5),
        price=product[3],
        payment_method=random.choice(PAYMENTS),
        city=fake.city(),
        country="India",
        order_status="PLACED",
        order_timestamp=datetime.utcnow()
    )
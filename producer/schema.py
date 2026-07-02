from pydantic import BaseModel
from datetime import datetime


class OrderEvent(BaseModel):
    order_id: str
    customer_id: str
    customer_name: str
    product_id: str
    product_name: str
    category: str
    quantity: int
    price: float
    payment_method: str
    city: str
    country: str
    order_status: str
    order_timestamp: datetime
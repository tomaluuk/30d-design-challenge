from decimal import Decimal
from dataclasses import dataclass
from enum import StrEnum, auto
from typing import Iterable


class OrderType(StrEnum):
    ONLINE = "online"
    IN_STORE = "in store"


class OrderStatus(StrEnum):
    IN_PROGRESS = auto()
    CONFIRMED = auto()
    SHIPPED = auto()


@dataclass
class Item:
    name: str
    price: Decimal


@dataclass
class Order:
    id: int
    type: OrderType
    customer_email: str
    status: OrderStatus = OrderStatus.IN_PROGRESS


@dataclass
class Email:
    body: str
    subject: str
    recipient: str
    sender: str


def calculate_price(items: Iterable[Item], discount: Decimal = Decimal(0)) -> Decimal:
    total_price = Decimal(sum(item.price for item in items))
    discounted_price = total_price - (total_price * discount)
    return discounted_price


def generate_order_email(order: Order) -> Email:
    message = f"Good news! Your order #{order.id} has been shipped and is on its way."
    subject = "Order Shipped"

    if order.status == OrderStatus.CONFIRMED:
        message = f"Thank you for your order! Your order #{order.id} has been confirmed."
        subject = "Order Confirmation"

    return Email(
        body=message,
        subject=subject,
        recipient=order.customer_email,
        sender="sales@webshop.com",
    )


def process_order(order: Order) -> None:
    # Logic to process an online order
    print(f"Processing {order.type} order...")

    if order.type == OrderType.ONLINE:
        print("Shipping the order...")
        order.status = OrderStatus.CONFIRMED

    else:
        print("Order ready for pickup.")
        order.status = OrderStatus.SHIPPED

    print(generate_order_email(order))
    print("Order processed successfully.")


def main() -> None:
    items = [
        Item(name="T-Shirt", price=Decimal("19.99")),
        Item(name="Jeans", price=Decimal("49.99")),
        Item(name="Shoes", price=Decimal("79.99")),
    ]

    online_order = Order(id=123, type=OrderType.ONLINE, customer_email="sarah@gmail.com")

    total_price = calculate_price(items)
    print("Total price:", total_price)

    discounted_price = calculate_price(items, Decimal("0.1"))
    print("Discounted price:", discounted_price)

    process_order(online_order)

    in_store_order = Order(id=456, type=OrderType.IN_STORE, customer_email="john@gmail.com")

    process_order(in_store_order)


if __name__ == "__main__":
    main()

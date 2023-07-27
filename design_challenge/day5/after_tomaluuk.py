from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Item:
    name: str
    price: Decimal
    quantity: int


def main():
    # Create a shopping cart
    items = [
        Item("Apple", Decimal("1.50"), 10),
        Item("Banana", Decimal("2.00"), 2),
        Item("Pizza", Decimal("11.90"), 5),
    ]

    total = sum(item.price * item.quantity for item in items)

    # Print the cart
    print("Shopping Cart:")
    print(f"{'Item'}{'Price':>14}{'Qty':>6}{'Total':>8}")
    for item in items:
        total_price = item.price * item.quantity
        print(f"{item.name:<8} $ {item.price:>6}{item.quantity:>6}  ${total_price:>6}")
    print("=" * 40)
    print(f"Total: $ {total}")


if __name__ == "__main__":
    main()

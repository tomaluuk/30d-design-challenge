from dataclasses import dataclass, field
from decimal import Decimal


@dataclass
class Item:
    name: str
    price: Decimal
    quantity: int

    @property
    def subtotal(self):
        return self.price * self.quantity


@dataclass
class ShoppingCart:
    items: list[Item] = field(default_factory=list)
    discount_code: str | None = None

    @property
    def total(self):
        return sum(item.price * item.quantity for item in self.items)


def main() -> None:
    # Create a shopping cart and add some items to it
    cart = ShoppingCart(
        items=[
            Item("Apple", Decimal("1.5"), 10),
            Item("Banana", Decimal("2"), 2),
            Item("Pizza", Decimal("11.90"), 5),
        ],
    )

    # Update some items' quantity and price
    cart.items[0].quantity = 10
    cart.items[2].price = Decimal("3.50")

    # Remove an item
    cart.items.remove(cart.items[1])

    print(cart.total)

    # Print the cart
    print("Shopping Cart:")
    print(f"{'Item':<10}{'Price':>10}{'Qty':>7}{'Total':>13}")
    for item in cart.items:
        print(f"{item.name:<12}${item.price:>7.2f}{item.quantity:>7}     ${item.subtotal:>7.2f}")
    print("=" * 40)
    print(f"Total: ${cart.total:>7.2f}")


if __name__ == "__main__":
    main()

from dataclasses import dataclass, field
from decimal import Decimal


class ItemNotFoundException(Exception):
    pass


@dataclass
class Item:
    name: str
    price: Decimal
    quantity: int

    @property
    def subtotal(self) -> Decimal:
        return self.price * self.quantity

    def set_quantity(self, quantity: int) -> None:
        self.quantity = quantity

    def set_price(self, price: Decimal) -> None:
        self.price = price


@dataclass
class ShoppingCart:
    items: list[Item] = field(default_factory=list)
    discount_code: str | None = None

    def __len__(self):
        return len(self.items)

    @property
    def total(self):
        return sum(item.subtotal for item in self.items)

    def find_item(self, name: str) -> Item:
        for item in self.items:
            if item.name == name:
                return item

        raise ItemNotFoundException(f"Item '{name}' not found.")

    def update_item(
        self, name: str, quantity: int | None = None, price: Decimal | None = None
    ) -> None:
        found_item = self.find_item(name)
        if quantity is not None:
            found_item.set_quantity(quantity)

        if price is not None:
            found_item.set_price(price)

    def remove_item(self, name) -> None:
        found_item = self.find_item(name)
        self.items.remove(found_item)

    def add_item(self, item: Item) -> None:
        self.items.append(item)


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
    cart.update_item("Apple", quantity=10)
    cart.update_item("Pizza", price=Decimal("3.50"))

    # Remove an item
    cart.remove_item("Banana")
    cart.add_item(Item("Burger", Decimal("7.90"), 2))

    # Print the cart
    print("Shopping Cart:")
    print(f"{'Item':<10}{'Price':>10}{'Qty':>7}{'Total':>13}")
    for item in cart.items:
        print(f"{item.name:<12}${item.price:>7.2f}{item.quantity:>7}     ${item.subtotal:>7.2f}")
    print("=" * 40)
    print(f"Total: ${cart.total:>7.2f}")


if __name__ == "__main__":
    main()

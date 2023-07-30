from dataclasses import dataclass, field
from decimal import Decimal


class ItemNotFoundException(Exception):
    def __init__(self, name, message="No item found with name"):
        self.name = name
        self.message = f"{message} '{self.name}'"
        super().__init__(self.message)


class InvalidQuantityException(Exception):
    def __init__(self, quantity, message="Quantity must be a positive integer."):
        self.quantity = quantity
        self.message = f"{message} Quantity given: {self.quantity}"
        super().__init__(self.message)


class InvalidPriceException(Exception):
    def __init__(self, price, message="Price must be a positive Decimal number."):
        self.price = price
        self.message = f"{message} Price given: {self.price}"
        super().__init__(self.message)


@dataclass
class Item:
    name: str
    price: Decimal
    quantity: int

    def __eq__(self, other) -> bool:
        return (
            self.name == other.name
            and self.price == other.price
            and self.quantity == other.quantity
        )

    @property
    def subtotal(self) -> Decimal:
        return self.price * self.quantity

    def set_quantity(self, quantity: int) -> None:
        if quantity <= 0:
            raise InvalidQuantityException(quantity)

        self.quantity = quantity

    def set_price(self, price: Decimal) -> None:
        if price <= Decimal(0):
            raise InvalidPriceException(price)

        self.price = price


@dataclass
class ShoppingCart:
    items: list[Item] = field(default_factory=list)
    discount_code: str | None = None

    def __len__(self):
        return len(self.items)

    def __str__(self) -> str:
        """Override string representation of the shopping cart."""

        # Use string concatenation due to indentation issues.
        output_str = (
            "Shopping Cart:\n"
            + f"{'Item':<10}{'Price':>10}{'Qty':>7}{'Total':>13}"
            + f"{self._get_items_str}\n"
            + f"{'=' * 40}\n"
            f"Total: ${self.total:>7.2f}\n"
        )
        return output_str

    @property
    def total(self):
        return sum(item.subtotal for item in self.items)

    @property
    def _get_items_str(self):
        items_str = ""
        for item in self.items:
            items_str += f"""\n{item.name:<12}${item.price:>7.2f}{item.quantity:>7}     ${item.subtotal:>7.2f}"""
        return items_str

    def find_item(self, name: str) -> Item:
        for item in self.items:
            if item.name == name:
                return item

        raise ItemNotFoundException(name)

    def update_item(
        self, name: str, quantity: int | None = None, price: Decimal | None = None
    ) -> None:
        found_item = self.find_item(name)
        try:
            if quantity is not None:
                found_item.set_quantity(quantity)

            if price is not None:
                found_item.set_price(price)

        except Exception as e:
            raise e

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

    print(cart)


if __name__ == "__main__":
    main()

from design_challenge.day6.after_tomaluuk import (
    ShoppingCart,
    Item,
    InvalidPriceException,
    InvalidQuantityException,
)
from decimal import Decimal
import random
import pytest


def generate_random_decimal(lower_limit: int, upper_limit: int) -> Decimal:
    """A helper function to simplify the generation of random numbers of type Decimal."""
    return Decimal(random.randrange(lower_limit, upper_limit) / 100)


def test_price_update():
    item_name = "Book"
    items = [
        Item(item_name, Decimal(14.5), 2),
    ]
    cart = ShoppingCart(items)

    for _ in range(1, 1000):
        cart.update_item(item_name, price=generate_random_decimal(1, 100))


def test_invalid_price_update():
    item_name = "Book"
    items = [
        Item(item_name, Decimal(14.5), 2),
    ]
    cart = ShoppingCart(items)
    with pytest.raises(InvalidPriceException):
        cart.update_item("Book", price=Decimal(0.0))

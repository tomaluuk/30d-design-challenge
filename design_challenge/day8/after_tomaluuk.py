from dataclasses import dataclass, field
from decimal import Decimal
from abc import ABC, abstractmethod
from typing import Optional


@dataclass
class Item:
    name: str
    price: Decimal
    quantity: int

    @property
    def subtotal(self) -> Decimal:
        return self.price * self.quantity


@dataclass
class Discount:
    amount: Decimal
    percentage: Decimal


DISCOUNTS = {
    "SAVE10": Discount(amount=Decimal("0"), percentage=Decimal("0.1")),
    "5BUCKSOFF": Discount(amount=Decimal("5.00"), percentage=Decimal("0")),
    "FREESHIPPING": Discount(amount=Decimal("2.00"), percentage=Decimal("0")),
    "BLKFRIDAY": Discount(amount=Decimal("0"), percentage=Decimal("0.2")),
}


class PaymentStrategy(ABC):
    @abstractmethod
    def process_payment(self):
        pass


class CCPayment(PaymentStrategy):
    def process_payment(self, total):
        card_number = input("Please enter your credit card number: ")
        expiration_date = input("Please enter your credit card expiration date: ")
        ccv = input("Please enter your credit card CCV: ")
        card_number_masked = card_number[-4:].rjust(len(card_number), "*")
        ccv_masked = len(ccv) * "*"
        print(
            f"Processing credit card payment of ${total:.2f} with card number {card_number_masked} and expiration date {expiration_date} and CCV {ccv_masked}..."
        )
        return 200


class PayPalPayment(PaymentStrategy):
    def process_payment(self, total):
        username = input("Please enter your PayPal username: ")
        password = input("Please enter your PayPal password: ")
        password_masked = len(password) * "*"
        print(
            f"Processing PayPal payment of ${total:.2f} with username {username} and password {password_masked}..."
        )


class ApplePayment(PaymentStrategy):
    def process_payment(self, total):
        device_id = input("Please enter your Apple Pay device ID: ")
        device_id_masked = device_id[-4:].rjust(len(device_id), "*")
        print(f"Processing Apple Pay payment of ${total:.2f} with device ID {device_id_masked}...")


PAYMENT_METHODS = {"cc": CCPayment(), "apple": ApplePayment(), "paypal": PayPalPayment()}


@dataclass
class ShoppingCart:
    items: list[Item] = field(default_factory=list)
    discounts: list[str] = field(default_factory=list)

    def add_item(self, item: Item) -> None:
        self.items.append(item)

    def remove_item(self, item_name: str) -> None:
        found_item = self.find_item(item_name)
        if not found_item:
            print(f"Item '{item_name}' not in shopping cart, can't remove it!")
        else:
            self.items.remove(found_item)

    def find_item(self, item_name: str) -> Item | None:
        for item in self.items:
            if item.name == item_name:
                return item
        return None

    @property
    def subtotal(self) -> Decimal:
        return Decimal(sum(item.subtotal for item in self.items))

    @property
    def total(self) -> Decimal:
        return self.subtotal - self.discount

    def apply_discount(self, code: str) -> None:
        if not code in DISCOUNTS:
            print(f"Discount code '{code}' is not valid!")
            return
        self.discounts.append(code)

    def remove_discount(self, code: str) -> None:
        self.discounts.remove(code)

    @property
    def discount(self) -> Decimal:
        total_discount = Decimal("0")
        for code in self.discounts:
            if code in DISCOUNTS:
                total_discount += DISCOUNTS[code].amount + (
                    DISCOUNTS[code].percentage * self.subtotal
                )
        return total_discount

    def display(self) -> None:
        print("Shopping Cart:")
        print(f"{'Item':<10}{'Price':>10}{'Qty':>7}{'Total':>13}")
        for item in self.items:
            print(
                f"{item.name:<12}${item.price:>7.2f}{item.quantity:>7}     ${item.subtotal:>7.2f}"
            )
        print("=" * 40)
        print(f"Subtotal: ${self.subtotal:>7.2f}")
        print(f"Discount: ${self.discount:>7.2f}")
        print(f"Total:    ${self.total:>7.2f}")

    def set_payment_method(self, payment_method: str) -> None:
        if payment_method in PAYMENT_METHODS:
            self.payment_method = payment_method

    def process_payment(self, payment_method) -> None:
        payment_method.process_payment(self.total)


def get_payment_method(payment_method):
    if payment_method in PAYMENT_METHODS.keys():
        return PAYMENT_METHODS[payment_method]
    else:
        print(f"Unknown payment type '{payment_method}'")


def request_payment_method():
    valid_input = False
    input_payment_method = ""
    while not valid_input:
        input_payment_method = input(
            "What payment method would you like to use? (cc/paypal/apple)\n> "
        )
        if input_payment_method in PAYMENT_METHODS.keys():
            valid_input = True
        else:
            print(f"Payment method '{input_payment_method}' is not valid.")
            print(f"Please choose one of the following: {[*PAYMENT_METHODS.keys()]}")
    return input_payment_method


def main() -> None:
    # Create a shopping cart and add some items to it
    cart = ShoppingCart(
        items=[
            Item("Apple", Decimal("1.50"), 10),
            Item("Banana", Decimal("2.00"), 2),
            Item("Pizza", Decimal("11.90"), 5),
        ],
    )
    cart.apply_discount("SAVE10")

    # Print the total
    cart.display()

    input_payment_method = request_payment_method()
    payment_method = get_payment_method(input_payment_method)
    cart.process_payment(payment_method)


if __name__ == "__main__":
    main()

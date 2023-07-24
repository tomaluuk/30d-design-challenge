from dataclasses import dataclass
from decimal import Decimal
from typing import Protocol


class PaymentService(Protocol):
    def set_api_key(self, api_key: str) -> None:
        ...

    def process_payment(self, amount: Decimal) -> None:
        ...

    def process_payout(self, amount: Decimal) -> None:
        ...


@dataclass
class StripePaymentService:
    api_key: str | None = None

    def set_api_key(self, api_key: str) -> None:
        print(f"Setting Stripe API key to {api_key}.")
        self.api_key = api_key

    def process_payment(self, amount: Decimal) -> None:
        print(f"Processing payment of {amount} via Stripe.")

    def process_payout(self, amount: Decimal) -> None:
        print(f"Processing payout of {amount} via Stripe.")

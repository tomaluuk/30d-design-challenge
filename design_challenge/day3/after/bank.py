from decimal import Decimal
from typing import Protocol
from dataclasses import dataclass
from enum import Enum, auto


class PaymentService(Protocol):
    def set_api_key(self, api_key: str) -> None:
        ...

    def process_payment(self, amount: Decimal) -> None:
        ...

    def process_payout(self, amount: Decimal) -> None:
        ...


class AccountType(Enum):
    SAVINGS = auto()
    CHECKING = auto()

    def __str__(self):
        return self.name.capitalize()


@dataclass
class Account:
    account_number: str
    balance: Decimal
    account_type: AccountType

    def deposit(
        self,
        amount: Decimal,
    ) -> None:
        print(f"Depositing {amount} into {self.account_type} Account {self.account_number}.")

        self.balance += amount

    def withdraw(self, amount: Decimal) -> None:
        print(f"Withdrawing {amount} from {self.account_type} Account {self.account_number}.")

        self.balance -= amount


def deposit(amount: Decimal, account: Account, payment_service: PaymentService) -> None:
    payment_service.process_payment(amount)
    account.deposit(amount)


def withdraw(amount: Decimal, account: Account, payment_service: PaymentService) -> None:
    payment_service.process_payout(amount)
    account.withdraw(amount)

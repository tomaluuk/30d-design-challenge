from dataclasses import dataclass
from decimal import Decimal
from typing import Protocol


@dataclass
class SavingsAccount:
    account_number: str
    balance: Decimal


@dataclass
class CheckingAccount:
    account_number: str
    balance: Decimal


class PaymentService(Protocol):
    def set_api_key(self, api_key: str) -> None:
        ...

    def process_payment(self, amount: Decimal) -> None:
        ...

    def process_payout(self, amount: Decimal) -> None:
        ...


class BankService:
    def __init__(self, payment_service: PaymentService):
        self.payment_service = payment_service

    def deposit(
        self,
        amount: Decimal,
        account: SavingsAccount | CheckingAccount,
    ) -> None:
        if isinstance(account, SavingsAccount):
            print(f"Depositing {amount} into Savings Account {account.account_number}.")
        else:
            print(f"Depositing {amount} into Checking Account {account.account_number}.")

        self.payment_service.process_payment(amount)
        account.balance += amount

    def withdraw(self, amount: Decimal, account: SavingsAccount | CheckingAccount) -> None:
        if isinstance(account, SavingsAccount):
            print(f"Withdrawing {amount} from Savings Account {account.account_number}.")
        else:
            print(f"Withdrawing {amount} from Checking Account {account.account_number}.")

        self.payment_service.process_payout(amount)
        account.balance -= amount

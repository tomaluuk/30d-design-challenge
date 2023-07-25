from decimal import Decimal
from dataclasses import dataclass
from abc import ABC


@dataclass
class Account(ABC):
    account_number: str
    balance: Decimal


@dataclass
class SavingsAccount(Account):
    account_number: str
    balance: Decimal


@dataclass
class CheckingAccount(Account):
    account_number: str
    balance: Decimal

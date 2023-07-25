from decimal import Decimal
from dataclasses import dataclass
from enum import Enum, auto


class AccountType(Enum):
    SAVINGS = auto()
    CHECKING = auto()


@dataclass
class Account:
    account_number: str
    balance: Decimal
    account_type: AccountType

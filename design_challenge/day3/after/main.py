from decimal import Decimal
from bank import Account, AccountType, withdraw, deposit
from stripe_service import StripePaymentService


def main() -> None:
    savings_account = Account("SA001", Decimal("1000"), AccountType.SAVINGS)
    checking_account = Account("CA001", Decimal("500"), AccountType.CHECKING)

    stripe_test_service = StripePaymentService(api_key="sk_test_1234567890")

    deposit(amount=Decimal("200"), account=savings_account, payment_service=stripe_test_service)
    deposit(amount=Decimal("300"), account=checking_account, payment_service=stripe_test_service)

    withdraw(amount=Decimal("100"), account=savings_account, payment_service=stripe_test_service)
    withdraw(amount=Decimal("200"), account=checking_account, payment_service=stripe_test_service)

    print(f"Savings Account Balance: {savings_account.balance}")
    print(f"Checking Account Balance: {checking_account.balance}")


if __name__ == "__main__":
    main()

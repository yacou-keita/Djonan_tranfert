

from app.features.bank.domain.usecases.create_account import CreateAccountParams
from app.features.bank.presentation.bank_services import BankService


def main():
    bankService = BankService()
    params = CreateAccountParams(name="SGBCI", password="1234")
    print(bankService.create_account(params))


main()

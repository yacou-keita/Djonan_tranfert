

from app.core.interface_usecase.interface_usecase import NoParams
from app.features.bank.domain.usecases.create_account import CreateAccountParams
from app.features.bank.presentation.bank_services import BankService


def main():
    bankService = BankService()
    params = CreateAccountParams(name="SGBCI", password="1234")
    bankService.create_account(params)
    print(bankService.get_account_list(NoParams))


main()

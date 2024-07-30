

from app.core.errors.failure import Failure
from app.core.interface_usecase.interface_usecase import NoParams
from app.features.bank.domain.entities.customer import Customer
from app.features.bank.domain.interface_repository.params import SubscribeParams
from app.features.bank.domain.usecases.create_account import CreateAccountParams
from app.features.bank.presentation.bank_services import BankService


def main():
    bankService = BankService()
    params = CreateAccountParams(name="SGBCI", password="1234")
    params1 = CreateAccountParams(name="BACI", password="1234")
    bankService.create_account(params)
    bankService.create_account(params1)

    customer = Customer(last_name="Yacou", fisrt_name="keita",
                        phoneNumber="0768223663")
    subcriber = SubscribeParams(customer, password="1234", bank_id=2)
    reponse = bankService.subscribe(params=subcriber)
    if isinstance(reponse, Failure):
        print(reponse)
        return
    # print(bankService.get_account_by_id(2))
    print(bankService.get_account_list(NoParams))


main()

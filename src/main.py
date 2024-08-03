

from app.core.errors.failure import Failure
from app.core.interface_usecase.interface_usecase import NoParams
from app.features.bank.domain.entities.customer import Customer
from app.features.bank.domain.interface_repository.params import LoginParams, SubscribeParams
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
    customer1 = Customer(last_name="Yacou", fisrt_name="keita",
                         phoneNumber="0768223663")
    subcriber1 = SubscribeParams(customer1, password="1234", bank_id=2)
    customer2 = Customer(last_name="Yacou", fisrt_name="keita",
                         phoneNumber="0268223663")
    subcriber2 = SubscribeParams(customer2, password="1234", bank_id=1)
    bankService.subscribe(params=subcriber)
    bankService.subscribe(params=subcriber1)
    bankService.subscribe(params=subcriber2)

    response = bankService.login(LoginParams(
    password="1234", phoneNumber="0768223663", bank_id=2))

    # print("init bank", bankService.get_account_by_id(2))
    # print(bankService.get_account_list(NoParams))
    print("Login",response)


main()

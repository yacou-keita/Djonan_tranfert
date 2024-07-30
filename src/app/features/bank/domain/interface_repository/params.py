from app.features.bank.domain.entities.customer import Customer


class CreateAccountParams:
    def __init__(self, name: str, password: str) -> None:
        self.name = name
        self.password = password


class SubscribeParams:
    def __init__(self, customer: Customer, password: str, bank_id: str) -> None:
        self.customer = customer
        self.password = password
        self.bank_id = bank_id

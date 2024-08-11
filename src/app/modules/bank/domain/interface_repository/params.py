from app.modules.bank.domain.entities.customer import Customer


class CreateAccountParams:
    def __init__(self, name: str, password: str) -> None:
        self.name = name
        self.password = password


class SubscribeParams:
    def __init__(self, customer: Customer, password: str, bank_id: str) -> None:
        self.customer = customer
        self.password = password
        self.bank_id = bank_id


class LoginParams:
    def __init__(self, password: str, phoneNumber: str, bank_id: str) -> None:
        self.password = password
        self.phoneNumber = phoneNumber
        self.bank_id = bank_id

    def __repr__(self) -> str:
        return f"LoginParams(password:{self.password} , phoneNumber:{self.phoneNumber} , bank_id:{self.bank_id})"

class Customer:
    def __init__(self, last_name: str, fisrt_name: str, phoneNumber: str) -> None:
        self.last_name = last_name
        self.fisrt_name = fisrt_name
        self.phoneNumber = phoneNumber
    def __repr__(self) -> str:
        return f"Customer(last_name:{self.last_name} , fisrt_name:{self.fisrt_name}, phoneNumber:{self.phoneNumber})"
        
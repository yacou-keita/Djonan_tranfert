class Failure:
    def __init__(self, message: str) -> None:
        self.message = message

    def __repr__(self) -> str:
        return f"Failure(message={self.message})"

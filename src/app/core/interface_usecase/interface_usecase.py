from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Union

from app.core.errors.failure import Failure


SuccessType = TypeVar("SuccessType")
Params = TypeVar("Params")


class IUseCase(ABC, Generic[SuccessType, Params]):

    @abstractmethod
    def execute(self, params: Params) -> Union[Failure, SuccessType]:
        pass


class NoParams:
    pass

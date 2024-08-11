from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.core.errors.failure import Failure
from app.core.interface_usecase.interface_usecase import NoParams
from app.modules.bank.data.data_source.mongoDB.mongoDB_data_source import MongoDBdataSource
from app.modules.bank.data.repository.bank_repository import BankRepository
from app.modules.bank.domain.interface_repository.params import CreateAccountParams
from app.modules.bank.presentation.bank_services import BankService


bank_router = APIRouter()

mongo_data_source = MongoDBdataSource()
bank_repository = BankRepository(mongo_data_source)
bank_service = BankService(bank_repository)


class CreateAccountParamsValidator(BaseModel):
    name: str
    password: str


@bank_router.post("/create/")
def run_create_account(params: CreateAccountParamsValidator):
    try:
        params = CreateAccountParams(
            name=params.name, password=params.password)
        response = bank_service.create_account(params)
        if isinstance(response, Failure):
            raise HTTPException(
                status_code=400, detail=response.message)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))


@bank_router.get("/banks/")
def run_get_account_list():
    return bank_service.get_account_list(NoParams)


@bank_router.get("/bank/{id}")
def run_get_account_list(id: str):
    response = bank_service.get_account_by_id(id)

    if isinstance(response, Failure):
        return response.message
    return response

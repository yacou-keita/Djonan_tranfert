from fastapi import FastAPI
import uvicorn
from app.modules.bank.presentation.fast_api.bank_controller import bank_router


djonan_transfert = FastAPI()


def include_router(app: FastAPI):
    app.include_router(bank_router)


include_router(djonan_transfert)

if __name__ == "__main__":
    uvicorn.run(djonan_transfert, host="127.0.0.1", port=8000, reload=True)

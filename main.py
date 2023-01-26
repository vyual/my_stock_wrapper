from fastapi import FastAPI, Depends
from fastapi.openapi.models import APIKey
from fastapi.security import OAuth2PasswordBearer

from loader import wrapper
from middlewares import auth

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/")
async def root():
    return "THERE IS A MY STOCK MICROSERVICE"


@app.get("/wholesale/{year}/{sklad}")
async def get_wholesale(year: int, sklad: str, api_key: APIKey = Depends(auth.get_api_key)):
    wholesale = await wrapper.get_all_sales_wholesale(year, sklad)
    return {"sum": int(wholesale["rows"][0]["sellSum"])/100}


@app.get("/all/{year}/{sklad}")
async def get_all(year: int, sklad: str, api_key: APIKey = Depends(auth.get_api_key)):
    all_ = await wrapper.get_all_sales(year, sklad)
    all_sum = 0
    for i in all_["series"]:
        all_sum += int(i["sum"])
    return {"sum": all_sum/100}


@app.get("/all_month/{year}/{month}/{sklad}")
async def get_all_month(year: int, month: int, sklad: str, api_key: APIKey = Depends(auth.get_api_key)):
    all_ = await wrapper.get_all_sales_month(year, month, sklad)
    all_sum = 0
    for i in all_["series"]:
        all_sum += int(i["sum"])
    return {"sum": all_sum/100}


@app.get("/wholesale_month/{year}/{month}/{sklad}")
async def get_wholesale_month(year: int, month: int, sklad: str, api_key: APIKey = Depends(auth.get_api_key)):
    wholesale = await wrapper.get_all_sales_wholesale_month(year, month, sklad)
    return {"sum": int(wholesale["rows"][0]["sellSum"])/100}
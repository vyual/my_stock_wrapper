from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer

from data.config import TOKEN
from loader import wrapper

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/")
async def root(token: str = Depends(oauth2_scheme)):
    return "THERE IS A MY STOCK MICROSERVICE"


@app.get("/wholesale/{token}/{year}/{sklad}")
async def get_wholesale(token: str, year: int, sklad: str):
    if token == TOKEN:
        wholesale = await wrapper.get_all_sales_wholesale(year, sklad)
        return {"sum": int(wholesale["rows"][0]["sellSum"])/100}
    else:
        return {"error": "token error"}


@app.get("/all/{token}/{year}/{sklad}")
async def get_all(token: str, year: int, sklad: str):
    if token == TOKEN:
        all_ = await wrapper.get_all_sales(year, sklad)
        all_sum = 0
        for i in all_["series"]:
            all_sum += int(i["sum"])
        return {"sum": all_sum/100}
    else:
        return {"error": "token error"}

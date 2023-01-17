from fastapi import FastAPI

from loader import wrapper

app = FastAPI()


@app.get("/")
async def root():
    return "THERE IS A MY STOCK MICROSERVICE"


@app.get("/wholesale/{year}/{sklad}")
async def get_wholesale(year: int, sklad: str):
    wholesale = await wrapper.get_all_sales_wholesale(year, sklad)
    return {"sum": wholesale["rows"][0]["sellSum"]}


@app.get("/all/{year}/{sklad}")
async def get_all(year: int, sklad: str):
    all_ = await wrapper.get_all_sales(year, sklad)
    all_sum = 0
    for i in all_["series"]:
        all_sum += int(i["sum"])
    return {"sum": all_sum}

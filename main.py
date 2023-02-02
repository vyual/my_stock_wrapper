from fastapi import FastAPI, Depends
from fastapi.openapi.models import APIKey
from fastapi.security import OAuth2PasswordBearer

from data.stocks import stocks_ids
from loader import wrapper
from middlewares import auth

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/")
async def root():
    return "THERE IS A MY STOCK MICROSERVICE"


@app.get("/tag/{agent_tag}/{start_date}/{end_date}/{sklad}")
async def get_sale_tag(agent_tag: str, start_date: str, end_date: str, sklad: str,
                       api_key: APIKey = Depends(auth.get_api_key)):
    sales_tag = await wrapper.get_all_sales_tag(agent_tag, start_date, end_date, sklad)
    all_sum = 0
    print(sales_tag)
    for i in sales_tag["rows"]:
        print(i)
        all_sum += int(i["sellSum"]) / 100
    return {"sum": all_sum}


@app.get("/all/{start_date}/{end_date}/{sklad}")
async def get_all(start_date: str, end_date: str, sklad: str, api_key: APIKey = Depends(auth.get_api_key)):
    all_ = await wrapper.get_all_sales(start_date, end_date, sklad)
    print(all_)
    all_sum = 0
    for i in all_["rows"]:
        print(i)
        all_sum += int(i["sellSum"]) / 100
    return {"sum": all_sum}


@app.get("/today/stocks")
async def get_today_dashboard_stocks(api_key: APIKey = Depends(auth.get_api_key)):
    resp_json = {}
    all_sum = 0
    profit_sum = 0
    for i in stocks_ids:
        print(i[1])
        today = await wrapper.get_all_sales_today(sklad=i[1])
        print(today)
        for x in today["rows"]:
            print(x)
            all_sum += int(x["sellSum"]) / 100
            profit_sum += int(x["profit"]) / 100
        resp_json[i[0]] = {"ПРОДАЖИ": all_sum,
                           "ПРИБЫЛЬНОСТЬ": profit_sum}
        all_sum = 0
        profit_sum = 0
    return {"resp": resp_json}


@app.get("/month/stocks")
async def get_month_dashboard_stocks(api_key: APIKey = Depends(auth.get_api_key)):
    resp_json = {}
    all_sum = 0
    profit_sum = 0
    for i in stocks_ids:
        print(i[1])
        today = await wrapper.get_all_sales_month(sklad=i[1])
        print(today)
        for x in today["rows"]:
            print(x)
            all_sum += int(x["sellSum"]) / 100
            profit_sum += int(x["profit"]) / 100
        resp_json[i[0]] = {"ПРОДАЖИ": all_sum,
                           "ПРИБЫЛЬНОСТЬ": profit_sum}
        all_sum = 0
        profit_sum = 0
    return {"resp": resp_json}

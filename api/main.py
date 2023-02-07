import aiohttp as aiohttp
from aiohttp import BasicAuth
from datetime import datetime, date


class MyStockWrapper:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.basic = BasicAuth(self.login, self.password)

    async def get_counterparty(self, offset):
        async with aiohttp.ClientSession() as session:
            url = f"https://online.moysklad.ru/api/remap/1.2/entity/counterparty/?offset={offset}&limit=1000"
            async with session.get(url, auth=self.basic) as resp:
                returned = await resp.json()

        return returned

    async def get_all_sales(self, start_date, end_date, sklad):
        async with aiohttp.ClientSession() as session:
            url = f"https://online.moysklad.ru/api/remap/1.2/report/profit/byemployee?momentFrom={start_date} 00:00:00&momentTo={end_date} 23:59:58&interval=day&filter=store=https://online.moysklad.ru/api/remap/1.2/entity/store/{sklad}/"
            print(url)
            async with session.get(url, auth=self.basic) as resp:
                returned = await resp.json()

        return returned

    async def get_all_sales_tag(self, agent_tag, start_date, end_date, sklad):
        async with aiohttp.ClientSession() as session:
            url = f"https://online.moysklad.ru/api/remap/1.2/report/profit/byemployee?filter=agentTag={agent_tag}&momentFrom={start_date} 00:00:00&momentTo={end_date} 23:59:59&interval=day&filter=store=https://online.moysklad.ru/api/remap/1.2/entity/store/{sklad}"
            async with session.get(url, auth=self.basic) as resp:
                returned = await resp.json()

        return returned

    async def get_all_sales_today(self, sklad):
        datetime.today().strftime('%Y-%m-%d')
        async with aiohttp.ClientSession() as session:
            url = f"https://online.moysklad.ru/api/remap/1.2/report/profit/byemployee?momentFrom={datetime.today().strftime('%Y-%m-%d')} 00:00:00&momentTo={datetime.today().strftime('%Y-%m-%d')} 23:59:58&interval=day&filter=store=https://online.moysklad.ru/api/remap/1.2/entity/store/{sklad}/"
            async with session.get(url, auth=self.basic) as resp:
                returned = await resp.json()

        return returned

    async def get_all_sales_month(self, sklad):
        month = date.today().month
        year = date.today().year
        if month < 10:
            month = int(f"0{month}")
        start_date = str(year) + '-' + str(month) + '-01'
        end_date = str(year) + '-' + str(month + 1) + '-01'
        async with aiohttp.ClientSession() as session:
            url = f"https://online.moysklad.ru/api/remap/1.2/report/profit/byemployee?momentFrom={start_date} 00:00:00&momentTo={end_date} 23:59:58&interval=day&filter=store=https://online.moysklad.ru/api/remap/1.2/entity/store/{sklad}/"
            async with session.get(url, auth=self.basic) as resp:
                returned = await resp.json()

        return returned

    async def get_all_sales_period(self, sklad, start_date, end_date):
        async with aiohttp.ClientSession() as session:
            url = f"https://online.moysklad.ru/api/remap/1.2/report/profit/byemployee?momentFrom={start_date} 00:00:00&momentTo={end_date} 23:59:58&interval=day&filter=store=https://online.moysklad.ru/api/remap/1.2/entity/store/{sklad}/"
            async with session.get(url, auth=self.basic) as resp:
                returned = await resp.json()

        return returned

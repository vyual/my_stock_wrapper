import aiohttp as aiohttp
from aiohttp import BasicAuth
from datetime import datetime


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
            url = f"https://online.moysklad.ru/api/remap/1.2/report/profit/byemployee?filter=agentTag={agent_tag}&momentFrom={start_date} 23:59:58&momentTo={end_date} 00:00:01&interval=day&filter=store=https://online.moysklad.ru/api/remap/1.2/entity/store/{sklad}"
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

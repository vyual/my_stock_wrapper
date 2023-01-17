import aiohttp as aiohttp
from aiohttp import BasicAuth


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

    async def get_all_sales(self, year, sklad):
        async with aiohttp.ClientSession() as session:
            url = f"https://online.moysklad.ru/api/remap/1.2/report/sales/plotseries?momentFrom={year}-01-01 00:00:00&momentTo={year + 1}-01-01 00:00:01&interval=month&filter=store=https://online.moysklad.ru/api/remap/1.2/entity/store/{sklad}/"
            async with session.get(url, auth=self.basic) as resp:
                returned = await resp.json()

        return returned

    async def get_all_sales_wholesale(self, year, sklad):
        async with aiohttp.ClientSession() as session:
            url = f"https://online.moysklad.ru/api/remap/1.2/report/profit/byemployee?filter=agentTag=%D0%BE%D0%BF%D1%82%D0%BE%D0%B2%D0%B8%D0%BA%D0%B8&momentFrom={year}-1-01%2000:00:00&momentTo={year + 1}-1-01%2000:00:01&interval=year&filter=store=https://online.moysklad.ru/api/remap/1.2/entity/store/{sklad}"
            async with session.get(url, auth=self.basic) as resp:
                returned = await resp.json()

        return returned

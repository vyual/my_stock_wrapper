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

    async def get_all_sales(self, start_date, end_date, sklad):
        async with aiohttp.ClientSession() as session:
            url = f"https://online.moysklad.ru/api/remap/1.2/report/profit/byemployee?momentFrom={start_date} 00:00:00&momentTo={end_date} 00:00:01&interval=day&filter=store=https://online.moysklad.ru/api/remap/1.2/entity/store/{sklad}/"
            print(url)
            async with session.get(url, auth=self.basic) as resp:
                returned = await resp.json()
        return returned

    async def get_all_sales_wholesale(self, start_date, end_date, sklad):
        async with aiohttp.ClientSession() as session:
            url = f"https://online.moysklad.ru/api/remap/1.2/report/profit/byemployee?filter=agentTag=оптовики&momentFrom={start_date} 00:00:01&momentTo={end_date} 00:00:01&interval=day&filter=store=https://online.moysklad.ru/api/remap/1.2/entity/store/{sklad}"
            async with session.get(url, auth=self.basic) as resp:
                returned = await resp.json()

        return returned

    # async def get_all_sales_month(self, year, month, sklad):
    #     async with aiohttp.ClientSession() as session:
    #         url = f"https://online.moysklad.ru/api/remap/1.2/report/sales/plotseries?momentFrom={year}-{month}-01 00:00:00&momentTo={year}-{month + 1}-01 00:00:01&interval=month&filter=store=https://online.moysklad.ru/api/remap/1.2/entity/store/{sklad}/"
    #         async with session.get(url, auth=self.basic) as resp:
    #             returned = await resp.json()
    #
    #     return returned
    #
    #
    # async def get_all_sales_wholesale_month(self, year, month, sklad):
    #     async with aiohttp.ClientSession() as session:
    #         url = f"https://online.moysklad.ru/api/remap/1.2/report/profit/byemployee?filter=agentTag=оптовики&momentFrom={year}-{month}-01%2000:00:00&momentTo={year}-{month + 1}-01%2000:00:01&interval=month&filter=store=https://online.moysklad.ru/api/remap/1.2/entity/store/{sklad}"
    #         async with session.get(url, auth=self.basic) as resp:
    #             returned = await resp.json()
    #
    #     return returned

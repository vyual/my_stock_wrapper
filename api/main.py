from datetime import datetime, date

import aiohttp as aiohttp
from aiohttp import BasicAuth


class MyStockWrapper:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.basic = BasicAuth(self.login, self.password)

    async def _make_request(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url, auth=self.basic) as resp:
                return await resp.json()

    async def get_counterparty(self, offset):
        url = f"https://online.moysklad.ru/api/remap/1.2/entity/counterparty/?offset={offset}&limit=1000"
        return await self._make_request(url)

    async def get_all_sales(self, start_date, end_date, sklad):
        url = f"https://online.moysklad.ru/api/remap/1.2/report/profit/byemployee?momentFrom={start_date} 00:00:00&momentTo={end_date} 23:59:58&interval=day&filter=store=https://online.moysklad.ru/api/remap/1.2/entity/store/{sklad}/"
        print(url)
        return await self._make_request(url)

    async def get_all_sales_tag(self, agent_tag, start_date, end_date, sklad):
        url = f"https://online.moysklad.ru/api/remap/1.2/report/profit/byemployee?filter=agentTag={agent_tag}&momentFrom={start_date} 00:00:00&momentTo={end_date} 23:59:59&interval=day&filter=store=https://online.moysklad.ru/api/remap/1.2/entity/store/{sklad}"
        return await self._make_request(url)

    async def get_all_sales_today(self, sklad):
        date_str = datetime.today().strftime('%Y-%m-%d')
        url = f"https://online.moysklad.ru/api/remap/1.2/report/profit/byemployee?momentFrom={date_str} 00:00:00&momentTo={date_str} 23:59:58&interval=day&filter=store=https://online.moysklad.ru/api/remap/1.2/entity/store/{sklad}/"
        return await self._make_request(url)

    async def get_all_sales_month(self, sklad):
        month = date.today().month
        year = date.today().year
        if month < 10:
            month = f"0{month}"
        start_date = f"{year}-{month}-01"
        end_date = f"{year}-{month + 1}-01"
        url = f"https://online.moysklad.ru/api/remap/1.2/report/profit/byemployee?momentFrom={start_date} 00:00:00&momentTo={end_date} 23:59:58&interval=day&filter=store=https://online.moysklad.ru/api/remap/1.2/entity/store/{sklad}/"
        return await self._make_request(url)

    async def get_all_sales_period(self, sklad, start_date, end_date):
        url = f"https://online.moysklad.ru/api/remap/1.2/report/profit/byemployee?momentFrom={start_date} 00:00:00&momentTo={end_date} 23:59:58&interval=day&filter=store=https://online.moysklad.ru/api/remap/1.2/entity/store/{sklad}/"
        return await self._make_request(url)

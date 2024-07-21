import aiohttp
from aiohttp import ClientSession, TCPConnector
import asyncio
import socket
import aiodns


async def fetch(url, dns_server=None):
    resolver = aiohttp.resolver.AsyncResolver(nameservers=[dns_server] if dns_server else None)
    connector = TCPConnector(resolver=resolver)

    async with ClientSession(connector=connector) as session:
        async with session.get(url) as response:
            return await response.text()


async def func(url, dns_server=None):
    resolver = aiohttp.resolver.AsyncResolver(nameservers=[dns_server] if dns_server else None)
    connector = TCPConnector(resolver=resolver)
    async with ClientSession(connector=connector) as session:
        async with session.get(url) as response:
            try:
                print(response.raise_for_status(), response.url)
                result = await response.json()
                print(result)
                result = await response.text()
                print(result)
            except (aiohttp.ClientError, socket.gaierror) as e:
                print(f"Failed to make a request to '{url}' using DNS server '{dns_server}'. Error: {e}")


def main_func(url_to_check):
    print('Проверка через Дефолтный DNS')
    asyncio.run(func(url_to_check))

    print('Проверка через Google DNS')
    asyncio.run(func(url_to_check, dns_server='8.8.8.8'))

    print('Проверка через Yandex DNS')
    asyncio.run(func(url_to_check, dns_server='77.88.8.1'))

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
# Пример использования
# url_to_check = 'https://iss.moex.com/iss/engines/stock/markets/bonds/securities/RU000A0JQ5W3/candleborders.json'
url_to_check = 'https://iss.moex.com/iss/engines/stock/markets/shares/securities/AFLT/candleborders.json'
main_func(url_to_check)
import asyncio

from boto3.dynamodb.conditions import Key
from httpx import AsyncClient
from pyperf import Runner

from aiodynamo.fast.client import FastClient
from aiodynamo.fast.credentials import Credentials
from aiodynamo.fast.http.httpx import HTTPX
from utils import TABLE_NAME, KEY_FIELD, KEY_VALUE, REGION_NAME


async def inner():
    async with AsyncClient() as http_client:
        client = FastClient(HTTPX(http_client), Credentials.auto(), REGION_NAME)
        items = [
            item
            async for item in client.query(TABLE_NAME, Key(KEY_FIELD).eq(KEY_VALUE))
        ]


def query_aiodynamo_httpx():
    asyncio.run(inner())


Runner().bench_func("query", query_aiodynamo_httpx)

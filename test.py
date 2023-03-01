import asyncio

from knockapi import AsyncKnock, Knock


async def co_test_fn():
    client = AsyncKnock(
        api_key="sk_z0fChGyRob55qhWxQkfbJqgdNRz9Bo0ZVLzdkeCz1Os"
    )

    print(await client.messages.list())


def test_fn():
    client = Knock(
        api_key="sk_z0fChGyRob55qhWxQkfbJqgdNRz9Bo0ZVLzdkeCz1Os"
    )

    print(client.messages.list())


asyncio.run(co_test_fn())
test_fn()


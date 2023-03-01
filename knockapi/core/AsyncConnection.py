import aiohttp

from json.decoder import JSONDecodeError


class AsyncConnection(object):

    def __init__(
        self,
        api_key: str,
        api_host: str,
        api_version: str,
        read_timeout: int
    ):
        self.api_key = api_key
        self.host = api_host
        self.client_version = api_version
        self.headers = {
            'Authorization': 'Bearer {}'.format(self.api_key),
            'User-Agent': 'Knock Python - {}'.format(self.client_version)
        }
        self.session = aiohttp.ClientSession(
            raise_for_status=True,
            headers=self.headers,
            read_timeout=read_timeout
        )

    async def request(self, method, endpoint, payload=None):
        async with self.session as client:
            url = '{}/v1{}'.format(self.host, endpoint)

            r = await client.request(
                method,
                url,
                params=payload if method == 'get' else None,
                json=payload if method != 'get' else None
            )

            async with r:

                # If we got a successful response, then attempt to deserialize as JSON
                if r.ok:
                    try:
                        return await r.json()
                    except JSONDecodeError:
                        return None

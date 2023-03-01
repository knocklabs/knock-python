import requests

from json.decoder import JSONDecodeError


class Connection(object):
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
        self.timeout = read_timeout
        self.headers = {
            'Authorization': 'Bearer {}'.format(self.api_key),
            'User-Agent': 'Knock Python - {}'.format(self.client_version)
        }
        self.session = requests.Session()

    def request(self, method, endpoint, payload=None):
        url = '{}/v1{}'.format(self.host, endpoint)

        r = self.session.request(
            method,
            url,
            params=payload if method == 'get' else None,
            json=payload if method != 'get' else None,
            headers=self.headers,
            timeout=self.timeout
        )

        # If we got a successful response, then attempt to deserialize as JSON
        if r.ok:
            try:
                return r.json()
            except JSONDecodeError:
                return None

        return r.raise_for_status()

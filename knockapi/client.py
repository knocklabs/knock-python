import requests

__version__ = '0.1.0'


class Connection(object):
    def __init__(self, api_key, host='https://api.knock.app'):
        self.api_key = api_key
        self.host = host
        self.client_version = __version__
        self.headers = {
            'Authorization': 'Bearer {}'.format(self.api_key),
            'User-Agent': 'Knock Python - {}'.format(self.client_version)
        }

    def request(self, method, endpoint, payload=None):
        url = '{}/v1{}'.format(self.host, endpoint)

        r = requests.request(
            method,
            url,
            json=payload,
            headers=self.headers,
        )

        if r.ok:
            return r.json()
        return r.raise_for_status()


class Knock(Connection):
    """Client to access the Knock features."""
    @property
    def _auth(self):
        return self.api_key

    @property
    def _version(self):
        return __version__

    @property
    def users(self):
        from .resources import User
        return User(self)

    def notify(self, name, actor, recipients, data={}):
        """
        Triggers a notification workflow.

        Args:
            name (str): The name of the notification to invoke.
            actor (str): The ID of the actor performing this action.
            recipients (array): An array of user IDs of who should be notified.
            data (dict): Any data to be passed to the notify call.

        Returns:
            dict: Response from Knock.
        """
        params = {
            'name': name,
            'actor': actor,
            'recipients': recipients,
            'data': data
        }
        return self.request("post", "/notify", payload=params)

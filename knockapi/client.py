import requests

__version__ = '0.1.1'


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

    def notify(self, name, actor, recipients, data={}, cancelation_key=None):
        """
        Triggers a notification workflow.

        Args:
            name (str): The name of the notification to invoke.
            actor (str): The ID of the actor performing this action.
            recipients (array): An array of user IDs of who should be notified.
            data (dict): Any data to be passed to the notify call.
            cancelation_key (str): A key used to cancel this notify.

        Returns:
            dict: Response from Knock.
        """
        params = {
            'name': name,
            'actor': actor,
            'recipients': recipients,
            'data': data,
            'cancelation_key': cancelation_key
        }
        return self.request("post", "/notify", payload=params)

    def cancel_notify(self, name, cancelation_key, recipients=None):
        """
        Cancels an in-flight notify call.

        Args:
            name (str): The name of the notification to invoke.
            cancelation_key (str): The key to identify the notify.
            recipients (array): An array of user IDs for recipients to cancel (can be omitted).

        Returns:
            dict: Response from Knock.
        """
        params = {
            'name': name,
            'recipients': recipients,
            'cancelation_key': cancelation_key
        }
        return self.request("post", "/notify/cancel", payload=params)

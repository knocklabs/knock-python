import requests

__version__ = '0.2.2'


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

    @property
    def workflows(self):
        from .resources import Workflows
        return Workflows(self)

    @property
    def preferences(self):
        from .resources import Preferences
        return Preferences(self)

    def notify(self, key, actor, recipients, data={}, cancellation_key=None, tenant=None):
        """
        Triggers a workflow.

        Args:
            key (str): The key of the workflow to invoke.
            actor (str): The ID of the actor performing this action.
            recipients (array): An array of user IDs of who should be notified.
            data (dict): Any data to be passed to the notify call.
            tenant (str): An optional identifier for the tenant object that the notifications
            cancellation_key (str): A key used to cancel this workflow.

        Returns:
            dict: Response from Knock.
        """
        # Note: this is essentially a delegated method
        return self.workflows.trigger(key, actor, recipients, data=data, cancellation_key=cancellation_key, tenant=tenant)

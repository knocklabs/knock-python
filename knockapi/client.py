import requests

__version__ = '0.4.2'


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

        # If we got a successful response, then attempt to deserialize as JSON
        if r.ok:
            try:
                return r.json()
            except ValueError:
                return None

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

    @property
    def objects(self):
        from .resources import Objects
        return Objects(self)

    @property
    def bulk_operations(self):
        from .resources import BulkOperations
        return BulkOperations(self)

    # Defined at the top level here for convienience
    def notify(self, key, actor, recipients, data={}, cancellation_key=None, tenant=None):
        """
        Triggers a workflow.

        Args:
            key (str): The key of the workflow to invoke.
            actor (str or dict): An optional reference for who/what performed the action.
            recipients (array): An array of recipient identifiers of who/what should be notified.
            data (dict): Any data to be passed to the notify call.
            tenant (str): An optional identifier for the tenant object that the notifications
            belong to.
            cancellation_key (str): A key used to cancel this notify.

        Returns:
            dict: Response from Knock.
        """
        # Note: this is essentially a delegated method
        return self.workflows.trigger(key, actor, recipients, data=data, cancellation_key=cancellation_key, tenant=tenant)

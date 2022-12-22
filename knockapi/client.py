import requests
from json.decoder import JSONDecodeError

__version__ = '0.5.1'


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
            params=payload,
            json=payload,
            headers=self.headers,
        )

        # If we got a successful response, then attempt to deserialize as JSON
        if r.ok:
            try:
                return r.json()
            except JSONDecodeError:
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
    def tenants(self):
        from .resources import Tenants
        return Tenants(self)

    @property
    def bulk_operations(self):
        from .resources import BulkOperations
        return BulkOperations(self)

    @property
    def messages(self):
        from .resources import Messages
        return Messages(self)

    # Defined at the top level here for convenience
    def notify(
            self,
            key,
            recipients,
            data={},
            actor=None,
            cancellation_key=None,
            tenant=None):
        """
        Triggers a workflow.

        Args:
            key (str): The key of the workflow to invoke.

            actor (str | dict[str, Any]): An optional reference for who/what performed the action. This can be A) a user
            id, B) an object reference, or C) a dictionary with data to identify a user or object.

            recipients (list[str | dict[str, Any]]): A list of recipients that should be notified. This can be a list of
            A) user ids, B) object references, C) dictionaries with data to identify a user or object, or D) a
            combination thereof.

            data (dict): Any data to be passed to the notify call.

            tenant (str): An optional identifier for the tenant that the notifications belong to.

            cancellation_key (str): A key used to cancel this notify.

        Returns:
            dict: Response from Knock.
        """
        # Note: this is essentially a delegated method
        return self.workflows.trigger(
            key=key,
            recipients=recipients,
            data=data,
            actor=actor,
            cancellation_key=cancellation_key,
            tenant=tenant)

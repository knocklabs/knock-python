from knockapi import __version__
from knockapi.core import AsyncConnection
from knockapi.async_client.services import User, Workflows, Preferences, Objects, Tenants, BulkOperations, Messages


class Knock(object):
    """Client to access the Knock features."""

    def __init__(
        self,
        api_key: str,
        api_host: str = 'https://api.knock.app',
        read_timeout: int = 300
    ):
        self.connection = AsyncConnection(
            api_key,
            api_host,
            __version__,
            read_timeout
        )

    @property
    def users(self):
        return User(self)

    @property
    def workflows(self):
        return Workflows(self)

    @property
    def preferences(self):
        return Preferences(self)

    @property
    def objects(self):
        return Objects(self)

    @property
    def tenants(self):
        return Tenants(self)

    @property
    def bulk_operations(self):
        return BulkOperations(self)

    @property
    def messages(self):
        return Messages(self)

    # Defined at the top level here for convenience
    async def notify(
        self,
        key,
        recipients,
        data={},
        actor=None,
        cancellation_key=None,
        tenant=None
    ):
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
        return await self.workflows.trigger(
            key=key,
            recipients=recipients,
            data=data,
            actor=actor,
            cancellation_key=cancellation_key,
            tenant=tenant
        )

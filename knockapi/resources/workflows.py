from .service import Service


class Workflows(Service):
    def trigger(self, key, actor, recipients, data={}, cancellation_key=None, tenant=None):
        """
        Triggers a workflow.

        Args:
            key (str): The key of the workflow to invoke.
            actor (str): The ID of the actor performing this action.
            recipients (array): An array of user IDs of who should be notified.
            data (dict): Any data to be passed to the notify call.
            tenant (str): An optional identifier for the tenant object that the notifications
            belong to.
            cancellation_key (str): A key used to cancel this notify.

        Returns:
            dict: Response from Knock.
        """
        endpoint = '/workflows/{}/trigger'.format(key)

        params = {
            'actor': actor,
            'recipients': recipients,
            'data': data,
            'cancellation_key': cancellation_key,
            'tenant': tenant
        }

        return self.request("post", endpoint, payload=params)

    def cancel(self, key, cancellation_key, recipients=None):
        """
        Cancels an in-flight workflow.

        Args:
            key (str): The workflow to cancel.
            cancellation_key (str): The key to identify the workflow.
            recipients (array): An array of user IDs for recipients to cancel (can be omitted).

        Returns:
            dict: Response from Knock.
        """
        endpoint = '/workflows/{}/cancel'.format(key)

        params = {
            'recipients': recipients,
            'cancellation_key': cancellation_key
        }

        return self.request("post", endpoint, payload=params)

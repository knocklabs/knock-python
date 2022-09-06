from .service import Service


class Workflows(Service):
    def trigger(
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

            tenant (str): An optional identifier for the tenant object that the notifications belong to.

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

        return self.client.request("post", endpoint, payload=params)

    def cancel(self, key, cancellation_key, recipients=None):
        """
        Cancels an in-flight workflow.

        Args:
            key (str): The workflow to cancel.
            cancellation_key (str): The key to identify the workflow.
            recipients (array): An array of recipient identifiers of who/what should be notified (can be omitted).

        Returns:
            dict: Response from Knock.
        """
        endpoint = '/workflows/{}/cancel'.format(key)

        params = {
            'recipients': recipients,
            'cancellation_key': cancellation_key
        }

        return self.client.request("post", endpoint, payload=params)

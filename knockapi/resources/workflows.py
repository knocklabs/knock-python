import datetime
from .service import Service


class Workflows(Service):
    def trigger(
            self,
            key,
            recipients,
            data={},
            actor=None,
            cancellation_key=None,
            tenant=None,
            options={}):
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

            options (dict): A dictionary of options to pass to the request (optional).
            Can include:
            - idempotency_key (str): An optional key that, if passed, will ensure that the same call is not made twice.

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

        return self.client.request("post", endpoint, payload=params, options=options)

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

    def create_schedules(
            self,
            key,
            recipients,
            repeats,
            data={},
            scheduled_at=datetime.datetime.now(),
            actor=None,
            tenant=None):
        """
        Creates schedules for recipients.

        Args:
            key (str): The key of the workflow to invoke.

            actor (str | dict[str, Any]): An optional reference for who/what performed the action. This can be A) a user
            id, B) an object reference, or C) a dictionary with data to identify a user or object.

            recipients (list[str | dict[str, Any]]): A list of recipients that should be notified. This can be a list of
            A) user ids, B) object references, C) dictionaries with data to identify a user or object, or D) a
            combination thereof.

            data (dict): Any data to be passed to the scheduled trigger call.

            scheduled_at (datetime): Date when the schedule must start

            tenant (str): An optional identifier for the tenant object that the notifications belong to.

        Returns:
            list[dict]: list of created schedules
        """
        endpoint = '/schedules'

        params = {
            'workflow': key,
            'recipients': recipients,
            'repeats': repeats,
            'actor': actor,
            'data': data,
            'tenant': tenant,
            'scheduled_at': scheduled_at.isoformat()
        }

        return self.client.request("post", endpoint, payload=params)

    def update_schedules(
            self,
            schedule_ids,
            schedule_attrs):
        """
        Updates schedules with given attributes.

        Args:
            schedule_ids (list[str]): the ids of the schedules to be updated (max 100)

            schedule_attrs (dict): Schedule attributes to be updated, these can be: repeats, actor, data and tenant.

        Returns:
            list[dict]: list of updated schedules
        """
        endpoint = '/schedules'

        schedule_attrs['schedule_ids'] = schedule_ids

        return self.client.request("put", endpoint, payload=schedule_attrs)

    def list_schedules(
            self,
            key,
            options = {}):
        """
        List workflow schedules

        Args:
            key (string): workflow key

            options (dict): Supports the following optional arguments:
                - page_size: specify size of the page to be returned by the api. (max limit: 50)
                - after:  after cursor for pagination
                - before: before cursor for pagination
                - tenant: tenant_id to filter schedules with
                - recipients: list of recipients to filter schedules with

        Returns:
            dict: list of updated schedules
        """

        endpoint = '/schedules'
        options['workflow'] = key

        return self.client.request('get', endpoint, payload=options)

    def delete_schedules(
            self,
            schedule_ids):
        """
        Delete schedules.

        Args:
            schedule_ids (list[str]): the ids of the schedules to be updated (max 100)

        Returns:
            list[dict]: list of updated schedules
        """
        endpoint = '/schedules'

        params = {
            'schedule_ids': schedule_ids,
        }

        return self.client.request("delete", endpoint, payload=params)

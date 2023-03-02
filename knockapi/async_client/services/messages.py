import json

from knockapi.core.Service import Service


class Messages(Service):

    async def list(self, options=None):
        """
        Gets a paginated list of Message records

        Args:
            options (dict): An optional set of filtering options to pass to the query

        Returns:
            dict: a paginated list of Message records
        """
        endpoint = '/messages'

        if options and options['trigger_data']:
            options['trigger_data'] = json.dumps(options['trigger_data'])

        return await self.client.connection.request('get', endpoint, payload=options)

    async def get(self, message_id):
        """
        Get a message by its id

        Args:
            message_id: The message ID

        Returns:
            dict: Message response from Knock.
        """
        endpoint = f'/messages/{message_id}'
        return await self.client.connection.request('get', endpoint)

    async def get_content(self, message_id):
        """
        Get a message's content by its id

        Args:
            message_id: The message ID

        Returns:
            dict: MessageContent response from Knock.
        """
        endpoint = f'/messages/{message_id}/content'
        return await self.client.connection.request('get', endpoint)

    async def get_activities(self, message_id, options=None):
        """
        Get a message's activities by its id

        Args:
            message_id: The message ID

        Returns:
            dict: paginated Activity response from Knock.
        """
        endpoint = f'/messages/{message_id}/activities'

        if options and options['trigger_data']:
            options['trigger_data'] = json.dumps(options['trigger_data'])

        return await self.client.connection.request('get', endpoint, options)

    async def get_events(self, message_id, options=None):
        """
        Get a message's events by its id

        Args:
            message_id: The message ID

        Returns:
            dict: paginated Event response from Knock.
        """
        endpoint = f'/messages/{message_id}/events'
        return await self.client.connection.request('get', endpoint, options)

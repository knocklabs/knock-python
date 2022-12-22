import json
from .service import Service

class Messages(Service):
    def list(self, options=None):
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

        return self.client.request('get', endpoint, payload=options)

    def get(self, id):
        """
        Get a message by its id

        Args:
            id: The message ID

        Returns:
            dict: Message response from Knock.
        """
        endpoint = '/messages/{}'.format(id)
        return self.client.request('get', endpoint)

    def get_content(self, id):
        """
        Get a message's content by its id

        Args:
            id: The message ID

        Returns:
            dict: MessageContent response from Knock.
        """
        endpoint = '/messages/{}/content'.format(id)
        return self.client.request('get', endpoint)

    def get_activities(self, id, options=None):
        """
        Get a message's activities by its id

        Args:
            id: The message ID

        Returns:
            dict: paginated Activity response from Knock.
        """
        endpoint = '/messages/{}/activities'.format(id)

        if options and options['trigger_data']:
            options['trigger_data'] = json.dumps(options['trigger_data'])

        return self.client.request('get', endpoint, options)

    def get_events(self, id, options=None):
        """
        Get a message's events by its id

        Args:
            id: The message ID

        Returns:
            dict: paginated Event response from Knock.
        """
        endpoint = '/messages/{}/events'.format(id)
        return self.client.request('get', endpoint, options)

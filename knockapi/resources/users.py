from .service import Service


class User(Service):
    def get_user(self, id):
        """
        Get a user by their id

        Args:
            id: The user ID

        Returns:
            dict: User response from Knock.
        """
        endpoint = '/users/{}'.format(id)
        return self.client.request('get', endpoint)

    def identify(self, id, data={}):
        """
        Identify a user, upserting them

        Args:
            id (str): The user ID
            data (dict): Other properties to put on the user

        Returns:
            dict: User response from Knock.
        """
        endpoint = '/users/{}'.format(id)
        return self.client.request('put', endpoint, payload=data)

    def delete(self, id):
        """
        Delets the given user.

        Args:
            id (str): The user ID

        Returns:
            dict: User response from Knock.
        """
        endpoint = '/users/{}'.format(id)
        return self.client.request('delete', endpoint)

    def get_channel_data(self, id, channel_id):
        """
        Get user's channel data for the given channel id.

        Args:
            id (str): The user ID
            channel_id (str): Target channel ID

        Returns:
            dict: Channel data from Knock.
        """
        endpoint = '/users/{}/channel_data/{}'.format(id, channel_id)
        return self.client.request('get', endpoint)

    def set_channel_data(self, id, channel_id, channel_data):
        """
        Upserts user's channel data for the given channel id.

        Args:
            id (str): The user ID
            channel_id (str): Target channel ID
            channel_data (dict): Channel data

        Returns:
            dict: Channel data from Knock.
        """
        endpoint = '/users/{}/channel_data/{}'.format(id, channel_id)
        return self.client.request('put', endpoint, payload={'data': channel_data})

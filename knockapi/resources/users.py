from .service import Service


class User(Service):
    def get_user(self, id):
        """
        Get a user by their id

        Args:
            id: The users ID

        Returns:
            dict: User response from Knock.
        """
        endpoint = '/users/{}'.format(id)
        return self.client.request('get', endpoint)

    def identify(self, id, data={}):
        """
        Identify a user, upserting them

        Args:
            id (str): The users ID
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
            id (str): The users ID

        Returns:
            dict: User response from Knock.
        """
        endpoint = '/users/{}'.format(id)
        return self.client.request('delete', endpoint)

from .service import Service

default_set_id = "default"


class Objects(Service):
    def get(self, collection, id):
        """
        Returns an object in a collection with the id given.

        Args:
            collection (str): The collection the object belongs to
            id (str): The id of the object in the collection

        Returns:
            dict: A Knock Object
        """
        endpoint = '/objects/{}/{}'.format(collection, id)
        return self.client.request('get', endpoint)

    # NOTE: This is `set_object` as `set` is a reserved keyword
    def set_object(self, collection, id, data = {}):
        """
        Returns an object in a collection with the id given.

        Args:
            collection (str): The collection the object belongs to
            id (str): The id of the object in the collection
            data (dict): The data to set on the object

        Returns:
            dict: A Knock Object
        """
        endpoint = '/objects/{}/{}'.format(collection, id)
        return self.client.request('put', endpoint, payload = data)

    def bulk_set(self, collection, objects):
        """
        Bulk sets up to 100 objects in a collection.

        Args:
            collection (str): The collection the object belongs to
            objects (array): The list of object dictionaries to set

        Returns:
            dict: BulkOperation from Knock
        """
        data = { 'objects': objects }
        endpoint = '/objects/{}/bulk/set'.format(collection)
        return self.client.request('post', endpoint, payload=data)

    def delete(self, collection, id):
        """
        Deletes the given object.

        Args:
            collection (str): The collection the object belongs to
            id (str): The id of the object in the collection

        Returns:
            None: No response
        """
        endpoint = '/objects/{}/{}'.format(collection, id)
        return self.client.request('delete', endpoint)

    def bulk_delete(self, collection, object_ids):
        """
        Bulk deletes up to 100 objects in a collection.

        Args:
            collection (str): The collection the object belongs to
            object_ids (array): The list of object ids to delete

        Returns:
            dict: BulkOperation from Knock
        """
        data = { 'object_ids': object_ids }
        endpoint = '/objects/{}/bulk/delete'.format(collection)
        return self.client.request('post', endpoint, payload=data)

    ##
    # Channel data
    ##

    def get_channel_data(self, collection, id, channel_id):
        """
        Get user's channel data for the given channel id.

        Args:
            collection (str): The collection the object belongs to
            id (str): The id of the object in the collection
            channel_id (str): Target channel ID

        Returns:
            dict: Channel data from Knock.
        """
        endpoint = '/objects/{}/{}/channel_data/{}'.format(collection, id, channel_id)
        return self.client.request('get', endpoint)

    def set_channel_data(self, collection, id, channel_id, channel_data):
        """
        Upserts user's channel data for the given channel id.

        Args:
            collection (str): The collection the object belongs to
            id (str): The id of the object in the collection
            channel_id (str): Target channel ID
            channel_data (dict): Channel data

        Returns:
            dict: Channel data from Knock.
        """
        endpoint = '/objects/{}/{}/channel_data/{}'.format(collection, id, channel_id)
        return self.client.request('put', endpoint, payload={'data': channel_data})
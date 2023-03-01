import json

from knockapi.core.Service import Service

default_set_id = "default"


class Objects(Service):

    async def get(self, collection, object_id):
        """
        Returns an object in a collection with the id given.

        Args:
            collection (str): The collection the object belongs to
            object_id (str): The id of the object in the collection

        Returns:
            dict: A Knock Object
        """
        endpoint = f'/objects/{collection}/{object_id}'
        return await self.client.connection.request('get', endpoint)

    # NOTE: This is `set_object` as `set` is a reserved keyword
    async def set_object(self, collection, object_id, data={}):
        """
        Returns an object in a collection with the id given.

        Args:
            collection (str): The collection the object belongs to
            object_id (str): The id of the object in the collection
            data (dict): The data to set on the object

        Returns:
            dict: A Knock Object
        """
        endpoint = f'/objects/{collection}/{object_id}'
        return await self.client.connection.request('put', endpoint, payload=data)

    async def bulk_set(self, collection, objects):
        """
        Bulk sets up to 100 objects in a collection.

        Args:
            collection (str): The collection the object belongs to
            objects (array): The list of object dictionaries to set

        Returns:
            dict: BulkOperation from Knock
        """
        data = {'objects': objects}
        endpoint = f'/objects/{collection}/bulk/set'
        return await self.client.connection.request('post', endpoint, payload=data)

    async def delete(self, collection, object_id):
        """
        Deletes the given object.

        Args:
            collection (str): The collection the object belongs to
            object_id (str): The id of the object in the collection

        Returns:
            None: No response
        """
        endpoint = f'/objects/{collection}/{object_id}'
        return await self.client.connection.request('delete', endpoint)

    async def bulk_delete(self, collection, object_ids):
        """
        Bulk deletes up to 100 objects in a collection.

        Args:
            collection (str): The collection the object belongs to
            object_ids (array): The list of object ids to delete

        Returns:
            dict: BulkOperation from Knock
        """
        data = {'object_ids': object_ids}
        endpoint = f'/objects/{collection}/bulk/delete'
        return await self.client.connection.request('post', endpoint, payload=data)

    ##
    # Channel data
    ##

    async def get_channel_data(self, collection, object_id, channel_id):
        """
        Get object's channel data for the given channel id.

        Args:
            collection (str): The collection the object belongs to
            object_id (str): The id of the object in the collection
            channel_id (str): Target channel ID

        Returns:
            dict: Channel data from Knock.
        """
        endpoint = f'/objects/{collection}/{object_id}/channel_data/{channel_id}'
        return await self.client.connection.request('get', endpoint)

    async def set_channel_data(self, collection, object_id, channel_id, channel_data):
        """
        Upserts object's channel data for the given channel id.

        Args:
            collection (str): The collection the object belongs to
            object_id (str): The id of the object in the collection
            channel_id (str): Target channel ID
            channel_data (dict): Channel data

        Returns:
            dict: Channel data from Knock.
        """
        endpoint = f'/objects/{collection}/{object_id}/channel_data/{channel_id}'
        return await self.client.connection.request(
            'put', endpoint, payload={
                'data': channel_data})

    async def unset_channel_data(self, collection, object_id, channel_id):
        """
        Unsets the object's channel data for the given channel id.

        Args:
            collection (str): The collection the object belongs to
            object_id (str): The id of the object in the collection
            channel_id (str): Target channel ID

        Returns:
            None: No response
        """
        endpoint = f'/objects/{collection}/{object_id}/channel_data/{channel_id}'
        return await self.client.connection.request('delete', endpoint)

    ##
    # Messages
    ##

    async def get_messages(self, collection, object_id, options=None):
        """
        Get object's messages

        Args:
            collection (str): The collection the object belongs to
            object_id (str): The id of the object in the collection
            options (dict): An optional set of filtering options to pass to the query

        Returns:
            dict: Paginated Message response.
        """
        endpoint = f'/objects/{collection}/{object_id}/messages'

        if options and options['trigger_data']:
            options['trigger_data'] = json.dumps(options['trigger_data'])

        return await self.client.connection.request('get', endpoint, payload=options)

    ##
    # Preferences
    ##

    async def get_all_preferences(self, collection, object_id):
        """
        Get an objects full set of preferences

        Args:
            collection (str): The collection the object belongs to
            object_id (str): The id of the object in the collection

        Returns:
            dict: PreferenceSet response from Knock.
        """
        endpoint = f'/objects/{collection}/{object_id}/preferences'
        return await self.client.connection.request('get', endpoint)

    async def get_preferences(self, collection, object_id, options={}):
        """
        Get a preference set

        Args:
            collection (str): The collection the object belongs to
            object_id (str): The id of the object in the collection
            options (dict):
                preference_set (str): The preference set to retrieve (defaults to "default")

        Returns:
            dict: PreferenceSet response from Knock.
        """
        preference_set_id = options.get('preference_set', default_set_id)
        endpoint = f'/objects/{collection}/{object_id}/preferences/{preference_set_id}'

        return await self.client.connection.request('get', endpoint)

    async def set_preferences(
            self,
            collection,
            object_id,
            channel_types=None,
            categories=None,
            workflows=None,
            options={}):
        """
        Sets the preference set

        Args:
            collection (str): The collection the object belongs to
            object_id (str): The id of the object in the collection
            channel_types (dict): A dictionary of channel type preferences
            categories (dict): A dictionary of category preferences
            workflows (dict): A dictionary of workflow preferences
            options (dict): A dictionary of options

        Returns:
            dict: PreferenceSet response from Knock.
        """
        preference_set_id = options.get('preference_set', default_set_id)

        endpoint = f'/objects/{collection}/{object_id}/preferences/{preference_set_id}'

        params = {
            'channel_types': channel_types,
            'categories': categories,
            'workflows': workflows
        }

        return await self.client.connection.request('put', endpoint, payload=params)

    async def set_channel_types_preferences(
            self, collection, object_id, preferences, options={}):
        """
        Sets the channel type preferences

        Args:
            collection (str): The collection the object belongs to
            object_id (str): The id of the object in the collection
            preferences (dict): A dictionary of channel type preferences
            options (dict): A dictionary of options

        Returns:
            dict: PreferenceSet response from Knock.
        """
        preference_set_id = options.get('preference_set', default_set_id)

        endpoint = f'/objects/{collection}/{object_id}/preferences/{preference_set_id}/channel_types'

        return await self.client.connection.request('put', endpoint, payload=preferences)

    async def set_channel_type_preferences(
            self,
            collection,
            object_id,
            channel_type,
            setting,
            options={}):
        """
        Sets the channel type preference

        Args:
            collection (str): The collection the object belongs to
            object_id (str): The id of the object in the collection
            channel_type (str): The channel_type to set
            setting (boolean): The preference setting
            options (dict): A dictionary of options

        Returns:
            dict: PreferenceSet response from Knock.
        """
        preference_set_id = options.get('preference_set', default_set_id)

        endpoint = f'/objects/{collection}/{object_id}/preferences/{preference_set_id}/channel_types/{channel_type}'

        return await self.client.connection.request(
            'put', endpoint, payload={
                'subscribed': setting})

    async def set_workflows_preferences(
            self,
            collection,
            object_id,
            preferences,
            options={}):
        """
        Sets the workflow preferences

        Args:
            collection (str): The collection the object belongs to
            object_id (str): The id of the object in the collection
            preferences (dict): A dictionary of workflow preferences
            options (dict): A dictionary of options

        Returns:
            dict: PreferenceSet response from Knock.
        """
        preference_set_id = options.get('preference_set', default_set_id)

        endpoint = f'/objects/{collection}/{object_id}/preferences/{preference_set_id}/workflows'

        return await self.client.connection.request('put', endpoint, payload=preferences)

    async def set_workflow_preferences(
            self,
            collection,
            object_id,
            key,
            setting,
            options={}):
        """
        Sets the workflow preferences

        Args:
            collection (str): The collection the object belongs to
            object_id (str): The id of the object in the collection
            key (str): The workflow key
            setting (boolean or dict): The preference setting
            options (dict): A dictionary of options

        Returns:
            dict: PreferenceSet response from Knock.
        """
        preference_set_id = options.get('preference_set', default_set_id)

        endpoint = f'/objects/{collection}/{object_id}/preferences/{preference_set_id}/workflows/{key}'

        params = setting if isinstance(setting, dict) else {
            'subscribed': setting}

        return await self.client.connection.request('put', endpoint, payload=params)

    async def set_categories_preferences(
            self,
            collection,
            object_id,
            preferences,
            options={}):
        """
        Sets the categories preferences

        Args:
            collection (str): The collection the object belongs to
            object_id (str): The id of the object in the collection
            preferences (dict): A dictionary of category preferences
            options (dict): A dictionary of options

        Returns:
            dict: PreferenceSet response from Knock.
        """
        preference_set_id = options.get('preference_set', default_set_id)

        endpoint = f'/objects/{collection}/{object_id}/preferences/{preference_set_id}/categories'

        return await self.client.connection.request('put', endpoint, payload=preferences)

    async def set_category_preferences(
            self,
            collection,
            object_id,
            key,
            setting,
            options={}):
        """
        Sets the category preferences

        Args:
            collection (str): The collection the object belongs to
            object_id (str): The id of the object in the collection
            key (str): The category key
            setting (boolean or dict): The preference setting
            options (dict): A dictionary of options

        Returns:
            dict: PreferenceSet response from Knock.
        """
        preference_set_id = options.get('preference_set', default_set_id)

        endpoint = f'/objects/{collection}/{object_id}/preferences/{preference_set_id}/categories/{key}'

        params = setting if isinstance(setting, dict) else {
            'subscribed': setting}

        return await self.client.connection.request('put', endpoint, payload=params)

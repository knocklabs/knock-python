import json
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
    def set_object(self, collection, id, data={}):
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
        return self.client.request('put', endpoint, payload=data)

    def bulk_set(self, collection, objects):
        """
        Bulk sets up to 100 objects in a collection.

        Args:
            collection (str): The collection the object belongs to
            objects (array): The list of object dictionaries to set

        Returns:
            dict: BulkOperation from Knock
        """
        data = {'objects': objects}
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
        data = {'object_ids': object_ids}
        endpoint = '/objects/{}/bulk/delete'.format(collection)
        return self.client.request('post', endpoint, payload=data)

    ##
    # Channel data
    ##

    def get_channel_data(self, collection, id, channel_id):
        """
        Get object's channel data for the given channel id.

        Args:
            collection (str): The collection the object belongs to
            id (str): The id of the object in the collection
            channel_id (str): Target channel ID

        Returns:
            dict: Channel data from Knock.
        """
        endpoint = '/objects/{}/{}/channel_data/{}'.format(
            collection, id, channel_id)
        return self.client.request('get', endpoint)

    def set_channel_data(self, collection, id, channel_id, channel_data):
        """
        Upserts object's channel data for the given channel id.

        Args:
            collection (str): The collection the object belongs to
            id (str): The id of the object in the collection
            channel_id (str): Target channel ID
            channel_data (dict): Channel data

        Returns:
            dict: Channel data from Knock.
        """
        endpoint = '/objects/{}/{}/channel_data/{}'.format(
            collection, id, channel_id)
        return self.client.request(
            'put', endpoint, payload={
                'data': channel_data})

    def unset_channel_data(self, collection, id, channel_id):
        """
        Unsets the object's channel data for the given channel id.

        Args:
            collection (str): The collection the object belongs to
            id (str): The id of the object in the collection
            channel_id (str): Target channel ID

        Returns:
            None: No response
        """
        endpoint = '/objects/{}/{}/channel_data/{}'.format(
            collection, id, channel_id)
        return self.client.request('delete', endpoint)

    ##
    # Messages
    ##

    def get_messages(self, collection, id, options=None):
        """
        Get object's messages

        Args:
            collection (str): The collection the object belongs to
            id (str): The id of the object in the collection
            options (dict): An optional set of filtering options to pass to the query

        Returns:
            dict: Paginated Message response.
        """
        endpoint = '/objects/{}/{}/messages'.format(collection, id)

        if options and options['trigger_data']:
            options['trigger_data'] = json.dumps(options['trigger_data'])

        return self.client.request('get', endpoint, payload=options)

    ##
    # Preferences
    ##

    def get_all_preferences(self, collection, id):
        """
        Get an objects full set of preferences

        Args:
            collection (str): The collection the object belongs to
            id (str): The id of the object in the collection

        Returns:
            dict: PreferenceSet response from Knock.
        """
        endpoint = '/objects/{}/{}/preferences'.format(collection, id)
        return self.client.request('get', endpoint)

    def get_preferences(self, collection, id, options={}):
        """
        Get a preference set

        Args:
            collection (str): The collection the object belongs to
            id (str): The id of the object in the collection
            options (dict):
                preference_set (str): The preference set to retrieve (defaults to "default")

        Returns:
            dict: PreferenceSet response from Knock.
        """
        preference_set_id = options.get('preference_set', default_set_id)
        endpoint = '/objects/{}/{}/preferences/{}'.format(
            collection, id, preference_set_id)

        return self.client.request('get', endpoint)

    def set_preferences(
            self,
            collection,
            id,
            channel_types=None,
            categories=None,
            workflows=None,
            options={}):
        """
        Sets the preference set

        Args:
            collection (str): The collection the object belongs to
            id (str): The id of the object in the collection
            channel_types (dict): A dictionary of channel type preferences
            categories (dict): A dictionary of category preferences
            workflows (dict): A dictionary of workflow preferences
            options (dict): A dictionary of options

        Returns:
            dict: PreferenceSet response from Knock.
        """
        preference_set_id = options.get('preference_set', default_set_id)

        endpoint = '/objects/{}/{}/preferences/{}'.format(
            collection, id, preference_set_id)

        params = {
            'channel_types': channel_types,
            'categories': categories,
            'workflows': workflows
        }

        return self.client.request('put', endpoint, payload=params)

    def set_channel_types_preferences(
            self, collection, id, preferences, options={}):
        """
        Sets the channel type preferences

        Args:
            collection (str): The collection the object belongs to
            id (str): The id of the object in the collection
            preferences (dict): A dictionary of channel type preferences
            options (dict): A dictionary of options

        Returns:
            dict: PreferenceSet response from Knock.
        """
        preference_set_id = options.get('preference_set', default_set_id)

        endpoint = '/objects/{}/{}/preferences/{}/channel_types'.format(
            collection, id, preference_set_id)

        return self.client.request('put', endpoint, payload=preferences)

    def set_channel_type_preferences(
            self,
            collection,
            id,
            channel_type,
            setting,
            options={}):
        """
        Sets the channel type preference

        Args:
            collection (str): The collection the object belongs to
            id (str): The id of the object in the collection
            channel_type (str): The channel_type to set
            setting (boolean): The preference setting
            options (dict): A dictionary of options

        Returns:
            dict: PreferenceSet response from Knock.
        """
        preference_set_id = options.get('preference_set', default_set_id)

        endpoint = '/objects/{}/{}/preferences/{}/channel_types/{}'.format(
            collection, id, preference_set_id, channel_type)

        return self.client.request(
            'put', endpoint, payload={
                'subscribed': setting})

    def set_workflows_preferences(
            self,
            collection,
            id,
            preferences,
            options={}):
        """
        Sets the workflow preferences

        Args:
            collection (str): The collection the object belongs to
            id (str): The id of the object in the collection
            preferences (dict): A dictionary of workflow preferences
            options (dict): A dictionary of options

        Returns:
            dict: PreferenceSet response from Knock.
        """
        preference_set_id = options.get('preference_set', default_set_id)

        endpoint = '/objects/{}/{}/preferences/{}/workflows'.format(
            collection, id, preference_set_id)

        return self.client.request('put', endpoint, payload=preferences)

    def set_workflow_preferences(
            self,
            collection,
            id,
            key,
            setting,
            options={}):
        """
        Sets the workflow preferences

        Args:
            collection (str): The collection the object belongs to
            id (str): The id of the object in the collection
            key (str): The workflow key
            setting (boolean or dict): The preference setting
            options (dict): A dictionary of options

        Returns:
            dict: PreferenceSet response from Knock.
        """
        preference_set_id = options.get('preference_set', default_set_id)

        endpoint = '/objects/{}/{}/preferences/{}/workflows/{}'.format(
            collection, id, preference_set_id, key)

        params = setting if isinstance(setting, dict) else {
            'subscribed': setting}

        return self.client.request('put', endpoint, payload=params)

    def set_categories_preferences(
            self,
            collection,
            id,
            preferences,
            options={}):
        """
        Sets the categories preferences

        Args:
            collection (str): The collection the object belongs to
            id (str): The id of the object in the collection
            preferences (dict): A dictionary of category preferences
            options (dict): A dictionary of options

        Returns:
            dict: PreferenceSet response from Knock.
        """
        preference_set_id = options.get('preference_set', default_set_id)

        endpoint = '/objects/{}/{}/preferences/{}/categories'.format(
            collection, id, preference_set_id)

        return self.client.request('put', endpoint, payload=preferences)

    def set_category_preferences(
            self,
            collection,
            id,
            key,
            setting,
            options={}):
        """
        Sets the category preferences

        Args:
            collection (str): The collection the object belongs to
            id (str): The id of the object in the collection
            key (str): The category key
            setting (boolean or dict): The preference setting
            options (dict): A dictionary of options

        Returns:
            dict: PreferenceSet response from Knock.
        """
        preference_set_id = options.get('preference_set', default_set_id)

        endpoint = '/objects/{}/{}/preferences/{}/categories/{}'.format(
            collection, id, preference_set_id, key)

        params = setting if isinstance(setting, dict) else {
            'subscribed': setting}

        return self.client.request('put', endpoint, payload=params)

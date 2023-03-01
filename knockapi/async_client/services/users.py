import json
from knockapi.core.Service import Service
from warnings import warn

default_set_id = "default"


class User(Service):

    async def get_user(self, user_id):
        warn("This method is deprecated. Use User.get instead.", DeprecationWarning, stacklevel=2)
        return await self.get(user_id)

    async def get(self, user_id):
        """
        Get a user by their id

        Args:
            user_id: The user ID

        Returns:
            dict: User response from Knock.
        """
        endpoint = f'/users/{user_id}'
        return await self.client.connection.request('get', endpoint)

    async def identify(self, user_id, data={}):
        """
        Identify a user, upserting them

        Args:
            user_id (str): The user ID
            data (dict): Other properties to put on the user

        Returns:
            dict: User response from Knock.
        """
        endpoint = f'/users/{user_id}'
        return await self.client.connection.request('put', endpoint, payload=data)

    async def bulk_identify(self, users):
        """
        Bulk identifies up to 100 users

        Args:
            users (array): The list of user dicts to upsert

        Returns
            dict: BulkOperation response from Knock.
        """
        endpoint = '/users/bulk/identify'
        data = {'users': users}
        return await self.client.connection.request('post', endpoint, payload=data)

    async def delete(self, user_id):
        """
        Deletes the given user.

        Args:
            user_id (str): The user ID

        Returns:
            None: No response
        """
        endpoint = f'/users/{user_id}'
        return await self.client.connection.request('delete', endpoint)

    async def bulk_delete(self, user_ids):
        """
        Bulk deletes up to 100 users.

        Args:
            user_ids (array): The list of user ids to upsert.

        Returns
            dict: BulkOperation response from Knock.
        """
        endpoint = '/users/bulk/delete'
        data = {'user_ids': user_ids}
        return await self.client.connection.request('post', endpoint, payload=data)

    async def get_feed(self, user_id, channel_id, options=None):
        """
        Gets a feed for the given user

        Args:
            user_id (str): The user ID
            channel_id (str): The ID of the feed channel
            options (dict): An optional set of feed options to pass to the query

        Returns
            dict: A Knock feed response
        """
        endpoint = f'/users/{user_id}/feeds/{channel_id}'

        if options and options['trigger_data']:
            options['trigger_data'] = json.dumps(options['trigger_data'])

        return await self.client.connection.request('get', endpoint, payload=options)

    async def merge(self, user_id, from_user_id):
        """
        Merges the user specified with `from_user_id` into the user specified with `user_id`.

        Args:
            user_id (str): The ID of the user to merge into
            from_user_id (str): The ID of the user to merge from

        Returns
            dict: A Knock User response
        """
        endpoint = f'/users/{user_id}/merge'
        data = {'from_user_id': from_user_id}
        return await self.client.connection.request('post', endpoint, payload=data)

    ##
    # Channel data
    ##

    async def get_channel_data(self, user_id, channel_id):
        """
        Get user's channel data for the given channel id.

        Args:
            user_id (str): The user ID
            channel_id (str): Target channel ID

        Returns:
            dict: Channel data from Knock.
        """
        endpoint = f'/users/{user_id}/channel_data/{channel_id}'
        return await self.client.connection.request('get', endpoint)

    async def set_channel_data(self, user_id, channel_id, channel_data):
        """
        Upserts user's channel data for the given channel id.

        Args:
            user_id (str): The user ID
            channel_id (str): Target channel ID
            channel_data (dict): Channel data

        Returns:
            dict: Channel data from Knock.
        """
        endpoint = f'/users/{user_id}/channel_data/{channel_id}'
        return await self.client.connection.request('put', endpoint, payload={'data': channel_data})

    async def unset_channel_data(self, user_id, channel_id):
        """
        Unsets the user's channel data for the given channel id.

        Args:
            user_id (str): The user ID
            channel_id (str): Target channel ID

        Returns:
            None: no response
        """
        endpoint = f'/users/{user_id}/channel_data/{channel_id}'
        return await self.client.connection.request('delete', endpoint)

    ##
    # Preferences
    ##

    async def get_all_preferences(self, user_id):
        """
        Get a users full set of preferences

        Args:
            user_id: The users ID

        Returns:
            dict: PreferenceSet response from Knock.
        """
        endpoint = f'/users/{user_id}/preferences'
        return await self.client.connection.request('get', endpoint)

    async def get_preferences(self, user_id, options={}):
        """
        Get a users preference set

        Args:
            user_id (str): The users ID
            options (dict):
                preference_set (str): The preference set to retrieve (defaults to "default")

        Returns:
            dict: PreferenceSet response from Knock.
        """
        preference_set_id = options.get('preference_set', default_set_id)
        endpoint = f'/users/{user_id}/preferences/{preference_set_id}'

        return await self.client.connection.request('get', endpoint)

    async def set_preferences(self, user_id, channel_types=None, categories=None, workflows=None, options={}):
        """
        Sets the preference set for the user

        Args:
            user_id (str): The users ID
            channel_types (dict): A dictionary of channel type preferences
            categories (dict): A dictionary of category preferences
            workflows (dict): A dictionary of workflow preferences
            options (dict): A dictionary of options

        Returns:
            dict: PreferenceSet response from Knock.
        """
        preference_set_id = options.get('preference_set', default_set_id)

        endpoint = f'/users/{user_id}/preferences/{preference_set_id}'

        params = {
            'channel_types': channel_types,
            'categories': categories,
            'workflows': workflows
        }

        return await self.client.connection.request('put', endpoint, payload=params)

    async def bulk_set_preferences(self, user_ids=[], preferences={}, options={}):
        """
        Bulk sets the preference set for the users given

        Args:
            user_ids (array): The users ids to apply the preferences to
            preferences (dict): The preferences to apply for the users
            options (dict): A dictionary of options

        Returns:
            dict: BulkOperation response from Knock.
        """
        endpoint = '/users/bulk/preferences'
        preference_set_id = options.get('preference_set', default_set_id)

        # Maybe set the default preference set id if it's not already set
        if 'id' not in preferences:
            preferences['id'] = preference_set_id

        params = {
            'preferences': preferences,
            'user_ids': user_ids,
        }

        return await self.client.connection.request('put', endpoint, payload=params)

    async def set_channel_types_preferences(self, user_id, preferences, options={}):
        """
        Sets the channel type preferences for the user

        Args:
            user_id (str): The users ID
            preferences (dict): A dictionary of channel type preferences
            options (dict): A dictionary of options

        Returns:
            dict: PreferenceSet response from Knock.
        """
        preference_set_id = options.get('preference_set', default_set_id)

        endpoint = f'/users/{user_id}/preferences/{preference_set_id}/channel_types'

        return await self.client.connection.request('put', endpoint, payload=preferences)

    async def set_channel_type_preferences(self, user_id, channel_type, setting, options={}):
        """
        Sets the channel type preference for the user

        Args:
            user_id (str): The users ID
            channel_type (str): The channel_type to set
            setting (boolean): The preference setting
            options (dict): A dictionary of options

        Returns:
            dict: PreferenceSet response from Knock.
        """
        preference_set_id = options.get('preference_set', default_set_id)

        endpoint = f'/users/{user_id}/preferences/{preference_set_id}/channel_types/{channel_type}'

        return await self.client.connection.request('put', endpoint, payload={'subscribed': setting})

    async def set_workflows_preferences(self, user_id, preferences, options={}):
        """
        Sets the workflow preferences for the user

        Args:
            user_id (str): The users ID
            preferences (dict): A dictionary of workflow preferences
            options (dict): A dictionary of options

        Returns:
            dict: PreferenceSet response from Knock.
        """
        preference_set_id = options.get('preference_set', default_set_id)

        endpoint = f'/users/{user_id}/preferences/{preference_set_id}/workflows'

        return await self.client.connection.request('put', endpoint, payload=preferences)

    async def set_workflow_preferences(self, user_id, key, setting, options={}):
        """
        Sets the workflow preferences for the user

        Args:
            user_id (str): The users ID
            key (str): The workflow key
            setting (boolean or dict): The preference setting
            options (dict): A dictionary of options

        Returns:
            dict: PreferenceSet response from Knock.
        """
        preference_set_id = options.get('preference_set', default_set_id)

        endpoint = f'/users/{user_id}/preferences/{preference_set_id}/workflows/{key}'

        params = setting if isinstance(setting, dict) else {'subscribed': setting}

        return await self.client.connection.request('put', endpoint, payload=params)

    async def set_categories_preferences(self, user_id, preferences, options={}):
        """
        Sets the categories preferences for the user

        Args:
            user_id (str): The users ID
            preferences (dict): A dictionary of category preferences
            options (dict): A dictionary of options

        Returns:
            dict: PreferenceSet response from Knock.
        """
        preference_set_id = options.get('preference_set', default_set_id)

        endpoint = f'/users/{user_id}/preferences/{preference_set_id}/categories'

        return await self.client.connection.request('put', endpoint, payload=preferences)

    async def set_category_preferences(self, user_id, key, setting, options={}):
        """
        Sets the category preferences for the user

        Args:
            user_id (str): The users ID
            key (str): The category key
            setting (boolean or dict): The preference setting
            options (dict): A dictionary of options

        Returns:
            dict: PreferenceSet response from Knock.
        """
        preference_set_id = options.get('preference_set', default_set_id)

        endpoint = f'/users/{user_id}/preferences/{preference_set_id}/categories/{key}'

        params = setting if isinstance(setting, dict) else {'subscribed': setting}

        return await self.client.connection.request('put', endpoint, payload=params)

    ##
    # Messages
    ##

    async def get_messages(self, user_id, options=None):
        """
        Get user's messages

        Args:
            user_id (str): The user ID
            options (dict): An optional set of filtering options to pass to the query

        Returns:
            dict: Paginated Message response.
        """
        endpoint = f'/users/{user_id}/messages'
        return await self.client.connection.request('get', endpoint, payload=options)

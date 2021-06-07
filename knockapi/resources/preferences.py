from .service import Service

default_set_id = "default"


class Preferences(Service):
    def get_all(self, user_id):
        """
        Get a users full set of preferences

        Args:
            user_id: The users ID

        Returns:
            dict: User response from Knock.
        """
        endpoint = '/users/{}/preferences'.format(user_id)
        return self.client.request('get', endpoint)

    def get(self, user_id, options={}):
        """
        Get a users preference set

        Args:
            user_id (str): The users ID
            options (dict):
                preference_set (str): The preference set to retrieve (defaults to "default")

        Returns:
            dict: User response from Knock.
        """
        preference_set_id = options.get('preference_set', default_set_id)
        endpoint = '/users/{}/preferences/{}'.format(
            user_id, preference_set_id)

        return self.client.request('get', endpoint)

    def update(self, user_id, channel_types=None, categories=None, workflows=None, options={}):
        """
        Sets the preference set for the user

        Args:
            user_id (str): The users ID
            channel_types (dict): A dictionary of channel type preferences
            categories (dict): A dictionary of category preferences
            workflows (dict): A dictionary of workflow preferences
            options (dict): A dictionary of options

        Returns:
            dict: User response from Knock.
        """
        preference_set_id = options.get('preference_set', default_set_id)

        endpoint = '/users/{}/preferences/{}'.format(
            user_id, preference_set_id)

        params = {
            'channel_types': channel_types,
            'categories': categories,
            'workflows': workflows
        }

        return self.client.request('put', endpoint, payload=params)

    def set_channel_types(self, user_id, preferences, options={}):
        """
        Sets the channel type preferences for the user

        Args:
            user_id (str): The users ID
            preferences (dict): A dictionary of channel type preferences
            options (dict): A dictionary of options

        Returns:
            dict: User response from Knock.
        """
        preference_set_id = options.get('preference_set', default_set_id)

        endpoint = '/users/{}/preferences/{}/channel_types'.format(
            user_id, preference_set_id)

        return self.client.request('put', endpoint, payload=preferences)

    def set_channel_type(self, user_id, channel_type, setting, options={}):
        """
        Sets the channel type preference for the user

        Args:
            user_id (str): The users ID
            channel_type (str): The channel_type to set
            setting (boolean): The preference setting 
            options (dict): A dictionary of options

        Returns:
            dict: User response from Knock.
        """
        preference_set_id = options.get('preference_set', default_set_id)

        endpoint = '/users/{}/preferences/{}/channel_types/{}'.format(
            user_id, preference_set_id, channel_type)

        return self.client.request('put', endpoint, payload={'subscribed': setting})

    def set_workflows(self, user_id, preferences, options={}):
        """
        Sets the workflow preferences for the user

        Args:
            user_id (str): The users ID
            preferences (dict): A dictionary of workflow preferences
            options (dict): A dictionary of options

        Returns:
            dict: User response from Knock.
        """
        preference_set_id = options.get('preference_set', default_set_id)

        endpoint = '/users/{}/preferences/{}/workflows'.format(
            user_id, preference_set_id)

        return self.client.request('put', endpoint, payload=preferences)

    def set_workflow(self, user_id, key, setting, options={}):
        """
        Sets the workflow preferences for the user

        Args:
            user_id (str): The users ID
            key (str): The workflow key
            setting (boolean or dict): The preference setting 
            options (dict): A dictionary of options

        Returns:
            dict: User response from Knock.
        """
        preference_set_id = options.get('preference_set', default_set_id)

        endpoint = '/users/{}/preferences/{}/workflows/{}'.format(
            user_id, preference_set_id, key)

        params = setting if type(setting) is dict else {'subscribed': setting}

        return self.client.request('put', endpoint, payload=params)

    def set_categories(self, user_id, preferences, options={}):
        """
        Sets the categories preferences for the user

        Args:
            user_id (str): The users ID
            preferences (dict): A dictionary of category preferences
            options (dict): A dictionary of options

        Returns:
            dict: User response from Knock.
        """
        preference_set_id = options.get('preference_set', default_set_id)

        endpoint = '/users/{}/preferences/{}/categories'.format(
            user_id, preference_set_id)

        return self.client.request('put', endpoint, payload=preferences)

    def set_category(self, user_id, key, setting, options={}):
        """
        Sets the category preferences for the user

        Args:
            user_id (str): The users ID
            key (str): The category key
            setting (boolean or dict): The preference setting 
            options (dict): A dictionary of options

        Returns:
            dict: User response from Knock.
        """
        preference_set_id = options.get('preference_set', default_set_id)

        endpoint = '/users/{}/preferences/{}/categories/{}'.format(
            user_id, preference_set_id, key)

        params = setting if type(setting) is dict else {'subscribed': setting}

        return self.client.request('put', endpoint, payload=params)

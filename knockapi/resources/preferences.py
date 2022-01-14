from .service import Service
from warnings import warn

class Preferences(Service):
    def get_all(self, user_id):
        warn("This method is deprecated. Use users.get_all_preferences instead.", DeprecationWarning, stacklevel=2)
        return self.client.users.get_all_preferences(user_id)

    def get(self, user_id, options={}):
        warn("This method is deprecated. Use users.get_preferences instead.", DeprecationWarning, stacklevel=2)
        return self.client.users.get_preferences(user_id, options)

    def update(self, user_id, channel_types=None, categories=None, workflows=None, options={}):
        warn("This method is deprecated. Use users.set_preferences instead.", DeprecationWarning, stacklevel=2)
        return self.client.users.set_preferences(user_id, channel_types=channel_types, categories=categories, workflows=workflows, options=options)

    def set_channel_types(self, user_id, preferences, options={}):
        warn("This method is deprecated. Use users.set_channel_types_preferences instead.", DeprecationWarning, stacklevel=2)
        return self.client.users.set_channel_types_preferences(user_id, preferences, options=options)

    def set_channel_type(self, user_id, channel_type, setting, options={}):
        warn("This method is deprecated. Use users.set_channel_type_preferences instead.", DeprecationWarning, stacklevel=2)
        return self.client.users.set_channel_types_preferences(user_id, channel_type, setting, options=options)

    def set_workflows(self, user_id, preferences, options={}):
        warn("This method is deprecated. Use users.set_workflows_preferences instead.", DeprecationWarning, stacklevel=2)
        return self.client.users.set_workflows_preferences(user_id, preferences, options=options)

    def set_workflow(self, user_id, key, setting, options={}):
        warn("This method is deprecated. Use users.set_workflow_preferences instead.", DeprecationWarning, stacklevel=2)
        return self.client.users.set_workflow_preferences(user_id, key, setting, setting, options=options)

    def set_categories(self, user_id, preferences, options={}):
        warn("This method is deprecated. Use users.set_categories_preferences instead.", DeprecationWarning, stacklevel=2)
        return self.client.users.set_categories_preferences(user_id, preferences, options=options)
        
    def set_category(self, user_id, key, setting, options={}):
        warn("This method is deprecated. Use users.set_category_preferences instead.", DeprecationWarning, stacklevel=2)
        return self.client.users.set_category_preferences(user_id, key, setting, setting, options=options)

from .service import Service


class Tenants(Service):
    def list(self):
        """
        Returns all tenants in the environment

        Args:
            None

        Returns:
            dict: A Knock Tenant
        """
        endpoint = '/tenants'
        return self.client.request('get', endpoint)

    def get(self, id):
        """
        Returns a tenant with the id given.

        Args:
            id (str): The id of the tenant

        Returns:
            dict: A Knock Tenant
        """
        endpoint = '/tenants/{}'.format(id)
        return self.client.request('get', endpoint)

    # NOTE: This is `set_tenant` as `set` is a reserved keyword
    def set_tenant(self, id, tenant_data={}):
        """
        Returns a tenant with the id given and updated settings.

        Args:
            id (str): The id of the tenant
            tenant_data (dict): The data to set on the tenant

        Returns:
            dict: A Knock Tenant
        """
        endpoint = '/tenants/{}'.format(id)
        return self.client.request('put', endpoint, payload=tenant_data)

    def delete(self, id):
        """
        Deletes the given tenant.

        Args:
            id (str): The id of the tenant

        Returns:
            None: No response
        """
        endpoint = '/tenants/{}'.format(id)
        return self.client.request('delete', endpoint)

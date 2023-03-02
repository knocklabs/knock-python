from knockapi.core.Service import Service


class Tenants(Service):

    async def list(self):
        """
        Returns all tenants in the environment

        Args:
            None

        Returns:
            dict: A Knock Tenant
        """
        endpoint = '/tenants'
        return await self.client.connection.request('get', endpoint)

    async def get(self, tenant_id):
        """
        Returns a tenant with the id given.

        Args:
            tenant_id (str): The id of the tenant

        Returns:
            dict: A Knock Tenant
        """
        endpoint = f'/tenants/{tenant_id}'
        return await self.client.connection.request('get', endpoint)

    # NOTE: This is `set_tenant` as `set` is a reserved keyword
    async def set_tenant(self, tenant_id, tenant_data={}):
        """
        Returns a tenant with the id given and updated settings.

        Args:
            tenant_id (str): The id of the tenant
            tenant_data (dict): The data to set on the tenant

        Returns:
            dict: A Knock Tenant
        """
        endpoint = f'/tenants/{tenant_id}'
        return await self.client.connection.request('put', endpoint, payload=tenant_data)

    async def delete(self, tenant_id):
        """
        Deletes the given tenant.

        Args:
            tenant_id (str): The id of the tenant

        Returns:
            None: No response
        """
        endpoint = f'/tenants/{tenant_id}'
        return await self.client.connection.request('delete', endpoint)

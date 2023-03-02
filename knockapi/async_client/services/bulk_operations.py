from knockapi.core.Service import Service

default_set_id = "default"


class BulkOperations(Service):

    async def get(self, bulk_operation_id):
        """
        Returns a bulk operation.

        Args:
            bulk_operation_id (str): The id of the bulk operation

        Returns:
            dict: A Knock BulkOperation
        """
        endpoint = f'/bulk_operations/{bulk_operation_id}'
        return await self.client.connection.request('get', endpoint)

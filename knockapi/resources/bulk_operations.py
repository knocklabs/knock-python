from .service import Service

default_set_id = "default"


class BulkOperations(Service):
    def get(self, id):
        """
        Returns an bulk operation.

        Args:
            id (str): The id of the bulk operation

        Returns:
            dict: A Knock BulkOperation
        """
        endpoint = '/bulk_operations/{}'.format(id)
        return self.client.request('get', endpoint)
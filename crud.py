from pymongo import MongoClient, errors

class CRUD:
    """ CRUD operations for a collection in MongoDB """

    def __init__(self, username, password, host, port, database, collection):
        self.client = MongoClient(f'mongodb://{username}:{password}@{host}:{port}')
        self.db = self.client[database]
        self.collection = self.db[collection]

    def create(self, document):
        """ Insert a document into the collection """
        if document:
            try:
                self.collection.insert_one(document)
                return True
            except errors.PyMongoError as e:
                print(f"Error during insertion: {e}")
                return False
        else:
            print("Provided document is empty, nothing to save")
            return False

    def read(self, query):
        """ Retrieve documents from the collection """
        try:
            results = list(self.collection.find(query))
            return results
        except errors.PyMongoError as e:
            print(f"Error during query: {e}")
            return []

    def update(self, query, new_values):
        """ Update documents in the collection """
        if query and new_values:
            try:
                result = self.collection.update_many(query, {'$set': new_values})
                return result.modified_count  # Return number of updated documents
            except errors.PyMongoError as e:
                print(f"Error during update: {e}")
                return 0
        else:
            print("Query or new values are empty, nothing to update")
            return 0

    def delete(self, query):
        """ Delete documents from the collection """
        if query:
            try:
                result = self.collection.delete_many(query)
                return result.deleted_count  # Return number of deleted documents
            except errors.PyMongoError as e:
                print(f"Error during deletion: {e}")
                return 0
        else:
            print("Query is empty, nothing to delete")
            return 0

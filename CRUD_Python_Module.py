# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from pymongo.errors import PyMongoError
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        USER = 'aacuser' 
        PASS = 'SNHU1234' 
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient(f'mongodb://{username}:{password}@{HOST}:{PORT}/?authSource=admin')
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 
        
            
    # Create method to implement the C in CRUD.                 
    def create(self, data: dict) -> bool:
        """
        Insert a document into the animals collection.

        :param data: dictionary containing document data
        :return: True if successful, False otherwise
        """
        try:
            if data is not None:
                self.collection.insert_one(data)  # data should be dictionary     
                return True
            else:
                print("Nothing to save, because data parameter is empty")
                return False

        except PyMongoError as e:
            print(f"Insert failed: {e}")
            return False

        
    # Read method to implement the R in CRUD.
    def read(self, query: dict) -> list:
        """
        Query documents from the animals collection.

        :param query: dictionary specifying query criteria
        :return: list of matching documents or empty list
        """
        try:
            if query is not None:
                cursor = self.collection.find(query)
                return list(cursor)  # convert cursor to list
            else:
                print("No query provided")
                return []

        except PyMongoError as e:
            print(f"Read failed: {e}")
            return []
        
        
    # Update method to implement the U in CRUD.
    def update(self, query: dict, new_values: dict) -> int:
        """
        Update documents in the animals collection.

        :param query: dictionary specifying which documents to update
        :param new_values: dictionary of values to update
        :return: number of documents modified
        """
        try:
            if query and new_values:
                result = self.collection.update_many(query, {"$set": new_values})
                return result.modified_count
            else:
                print("Invalid query or update values")
                return 0

        except PyMongoError as e:
            print(f"Update failed: {e}")
            return 0


    # Delete method to implement the D in CRUD.
    def delete(self, query: dict) -> int:
        """
        Delete documents from the animals collection.

        :param query: dictionary specifying which documents to delete
        :return: number of documents deleted
        """
        try:
            if query:
                result = self.collection.delete_many(query)
                return result.deleted_count
            else:
                print("No query provided")
                return 0

        except PyMongoError as e:
            print(f"Delete failed: {e}")
            return 0
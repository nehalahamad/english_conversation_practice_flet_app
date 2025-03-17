from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, PyMongoError
import os


class MongoDBHandler:
    def __init__(self, connection_string, database_name):
        """
        Initialize the MongoDBHandler with a connection string and database name.
        """
        self.connection_string = connection_string
        self.database_name = database_name
        self.client = None
        self.db = None

        try:
            # Attempt to connect to MongoDB
            self.client = MongoClient(self.connection_string)
            self.db = self.client[self.database_name]
            print("Connected to MongoDB successfully!")
        except ConnectionFailure as e:
            print(f"Failed to connect to MongoDB: {e}")
            raise  # Re-raise the exception to stop further execution

    def insert_record(self, collection_name, record):
        """
        Insert a single record into the specified collection.
        """
        try:
            collection = self.db[collection_name]
            result = collection.insert_one(record)
            print(f"Inserted single record with id: {result.inserted_id}")
            return result.inserted_id
        except PyMongoError as e:
            print(f"Error inserting record: {e}")
            return None

    def insert_many_records(self, collection_name, records):
        """
        Insert multiple records into the specified collection.
        """
        try:
            collection = self.db[collection_name]
            result = collection.insert_many(records)
            print(f"Inserted multiple records with ids: {result.inserted_ids}")
            return result.inserted_ids
        except PyMongoError as e:
            print(f"Error inserting records: {e}")
            return None

    def find_all_records(self, collection_name):
        """
        Retrieve all records from the specified collection.
        """
        try:
            collection = self.db[collection_name]
            records = list(collection.find())  # Convert cursor to a list
            print(f"Found {len(records)} records in collection '{collection_name}'.")
            return records
        except PyMongoError as e:
            print(f"Error finding records: {e}")
            return None

    def close_connection(self):
        """
        Close the MongoDB connection.
        """
        if self.client:
            self.client.close()
            print("MongoDB connection closed.")


# Example usage
if __name__ == "__main__":
    # MongoDB connection details
    connection_string = "mongodb://localhost:27017/"
    database_name = "mydatabase"

    # Create an instance of MongoDBHandler
    mongo_handler = None
    try:
        mongo_handler = MongoDBHandler(connection_string, database_name)

        # Insert a single record
        single_record = {
            "name": "John Doe",
            "age": 30,
            "email": "johndoe@example.com"
        }
        inserted_id = mongo_handler.insert_record("mycollection", single_record)
        if inserted_id:
            print(f"Successfully inserted single record with id: {inserted_id}")

        # Insert multiple records
        multiple_records = [
            {
                "name": "Jane Doe",
                "age": 25,
                "email": "janedoe@example.com"
            },
            {
                "name": "Alice",
                "age": 28,
                "email": "alice@example.com"
            }
        ]
        inserted_ids = mongo_handler.insert_many_records("mycollection", multiple_records)
        if inserted_ids:
            print(f"Successfully inserted multiple records with ids: {inserted_ids}")

        # Find all records in the collection
        all_records = mongo_handler.find_all_records("mycollection")
        if all_records:
            print("All records in the collection:")
            for record in all_records:
                print(record)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Ensure the connection is closed
        if mongo_handler:
            mongo_handler.close_connection()
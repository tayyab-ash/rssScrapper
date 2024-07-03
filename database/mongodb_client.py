# import motor.motor_asyncio


# class MongoDBClient:
#     def __init__(self, database_name, uri):
#         self.client = motor.motor_asyncio.AsyncIOMotorClient(uri)
#         self.db = self.client.get_database(database_name)

#     async def insert_document(self, collection_name, document):
#         record_id = document['_id']

#         collection = self.db[collection_name]
#         result = await collection.insert_one(document)
#         return result.inserted_id

#     def close(self):
#         self.client.close()

import motor.motor_asyncio

class MongoDBClient:
    def __init__(self, database_name, uri):
        self.client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self.client.get_database(database_name)

    async def insert_document(self, collection_name, document):
        record_id = document['_id']
        
        collection = self.db[collection_name]
        
        # Check if the document already exists
        existing_document = await collection.find_one({'_id': record_id})
        if existing_document:
            return f"Document with _id {record_id} already exists"
        
        # Insert the document if it doesn't exist
        result = await collection.insert_one(document)
        return result.inserted_id

    def close(self):
        self.client.close()

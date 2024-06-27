import motor.motor_asyncio


class MongoDBClient:
    def __init__(self, database_name, uri):
        self.client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self.client.get_database(database_name)

    async def insert_document(self, collection_name, document):
        collection = self.db[collection_name]
        result = await collection.insert_one(document)
        return result.inserted_id

    def close(self):
        self.client.close()

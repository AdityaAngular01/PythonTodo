from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import env as ENV


class MongoDB:
    client: AsyncIOMotorClient = None
    database = None


mongodb = MongoDB()


async def connect_to_db():
    mongodb.client = AsyncIOMotorClient(ENV.MONGO_URL)
    mongodb.database = mongodb.client[ENV.DATABASE_NAME]
    print("✅ Connected to MongoDB")


async def disconnect_from_db():
    if mongodb.client:
        mongodb.client.close()
        print("❌ Disconnected from MongoDB")


# ✅ Use this anywhere
def user_collection():
    if mongodb.database is None:
        raise Exception("Database not initialized. Did you forget startup event?")
    return mongodb.database.get_collection("users")
from pymongo import MongoClient
import os
from dotenv import load_dotenv


load_dotenv()

try:
    client = MongoClient(os.getenv("MONGODB_URI"))
    print('client created')
    db = client["ecpdb"]
    collection = db["ecp"]

    english_conversation_practice = collection.find()

    print(len(list(english_conversation_practice)))
except:
    pass

finally:
    try:
        client.close()
    except:
        pass
import sys
import os
from pathlib import Path
from pymongo import MongoClient
from dotenv import load_dotenv

# Add project root to Python path
project_root = str(Path(__file__).parent.parent)
sys.path.append(project_root)

from src.my_utility.my_functions import load_json_data

# Load environment variables from a .env file
load_dotenv()

# Step 1: Connect to MongoDB
# Replace the connection string with your MongoDB connection string
client = MongoClient(os.getenv("MONGODB_URI"))

# Step 2: Create or access a database
db = client["ecpdb"]

# Step 3: Create or access a collection within the database
collection = db["ecp"]

# Step 4: Insert a single record (document) into the collection
ecp_data = load_json_data("etl/data/english_conversation_practice.json")


# Step 5: Insert multiple records (documents) into the collection
insert_many_result = collection.insert_many(ecp_data)
print(f"Inserted records with ids: {insert_many_result.inserted_ids}")

# Step 6: Close the connection (optional, as the connection is closed automatically when the script ends)
client.close()
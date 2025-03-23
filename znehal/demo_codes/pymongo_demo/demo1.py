from pymongolite import MongoClient



my_db_dir = "C:/ZMyCodes/english_conversation_practice_flet_app/znehal/demo_codes/pymongo_demo"


with MongoClient(dirpath=my_db_dir, database="quizz_db") as client:
    db = client.get_default_database()
    # collection = db.get_collection("users")
    collection = db.create_collection("users")

    collection.insert_one({"name": "yoyo"})
    collection.update_one({"name": "yoyo"}, {"$set": {"age": 20}})
    user = collection.find_one({"age": 20})
    print(user) # -> {"_id": ObjectId(...), "name": "yoyo", "age": 20}
from pymongolite import MongoClient
import json

my_db_dir = r"C:\ZMyCodes\english_conversation_practice_flet_app\src\assets"

client = MongoClient(dirpath=my_db_dir, database="quizzdb")

db = client.get_default_database()

files = [
    (r"src\assets\docker_question_new.json", "docker_quizz"),
    (r"src\assets\git_question_new.json", "git_quizz"),
    (r"src\assets\kubernetes_question_new.json", "kubernetes_quizz"),
    (r"src\assets\linux_question_new.json", "linux_quizz"),
    (r"src\assets\mongodb_question_new.json", "mongodb_quizz"),
    (r"src\assets\regex_python_question_new.json", "regex_python_quizz")
]

for file_name, collection_name in files:
    with open(file_name, 'r', encoding='utf-8') as file:
        questions_json = json.load(file)
    
    collection = db.create_collection(collection_name)
    collection.insert_many(questions_json)

client.close()
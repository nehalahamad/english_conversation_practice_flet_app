import requests
from bs4 import BeautifulSoup
import json

# URL of the page to scrape
url = "https://www.sanfoundry.com/linux-environment-mcq-1/"

# Send a GET request to the URL
response = requests.get(url)
print(response)
soup = BeautifulSoup(response.content, "html.parser")

# Find all question containers
questions = soup.find_all("div", class_="entry-content")

# Initialize an empty list to store the MCQ data
mcq_data = []

# Loop through each question and extract details
for i, question in enumerate(questions):
    # Extract the question text
    question_text = question.find("p").text.strip()
    
    # Extract options (A, B, C, D)
    options = {}
    option_tags = question.find_all("li")
    for j, option in enumerate(option_tags):
        options[chr(65 + j)] = option.text.strip()
    
    # Extract the correct answer
    answer_tag = question.find("div", class_="collapseomatic_content")
    answer = answer_tag.text.strip().split("Answer: ")[1].strip() if answer_tag else ""
    
    # Extract the explanation (if available)
    explanation = answer_tag.text.strip() if answer_tag else ""
    
    # Append the data to the list
    mcq_data.append({
        "QN": i + 1,
        "type": "mcq",
        "question": question_text,
        "options": options,
        "answer": answer,
        "explanation": explanation
    })

# Convert the list to JSON format
json_output = json.dumps(mcq_data, indent=4)

# Save the JSON to a file or print it
with open("mcq_questions.json", "w") as f:
    f.write(json_output)

print(json_output)
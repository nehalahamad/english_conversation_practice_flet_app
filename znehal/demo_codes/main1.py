import pdfplumber

# Open the PDF file
with pdfplumber.open('EnglishConversationPractice-pdfcoffee.pdf') as pdf:
    text = ""
    # Iterate through each page and extract text
    for page in pdf.pages:
        text += page.extract_text()
    
    # Print or process the text (assuming it's UTF-8 encoded)
    
with open(file="Output_1.txt", mode="w", encoding='utf-8') as text_file:
    text_file.write(text)
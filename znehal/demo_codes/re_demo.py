import re

# Sample text
text = "This is a 'sample' text with 'multiple' single quoted 'words'. Using the pattern '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$'"

# Regular expression to find anything between single inverted commas
pattern = r"'(.*?)'"

# Find all matches
matches = re.findall(pattern, text)

# Print the matches
print(matches)
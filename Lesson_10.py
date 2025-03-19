# Lesson 10: File Handling

# Writing and reading from a JSON file
import json

data = {"name": "Aleha", "age": 18, "city": "Karachi"}

# Writing to JSON file
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

# Reading from JSON file
with open("data.json", "r") as file:
    content = json.load(file)
    print("File Content:", content)
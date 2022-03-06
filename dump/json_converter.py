import json
from pprint import pprint

data = []

file_name = input("Dump file name: ")
output_name = input("Output file to append to: ")
# Files included:
# add dump/ if started from git root

# xkaubu_no_replies_1.json
# xkaubu_no_replies_2.json
# xkaubu_no_replies_3.json
# xkaubu_no_replies_4.json

# dump/xkaubu_no_replies_1.json
# dump/xkaubu_no_replies_2.json
# dump/xkaubu_no_replies_3.json
# dump/xkaubu_no_replies_4.json

# dump/xkaubu_no_replies.txt

print("Loading JSON file...")
with open(file_name) as f:
    data.append(json.load(f))

# Shadow variable 'data' with first item in data list
data = data[0]
# Get only the 'data' section of the JSON
data = data["data"]

print("Opening file...")
# Loop through the data
with open(output_name, "a") as f:
    messages = []
    
    print("Getting messages from JSON...")
    
    for message in data:
        messages.append(message["text"])
    
    print("Writing to file...")
    f.writelines(messages)
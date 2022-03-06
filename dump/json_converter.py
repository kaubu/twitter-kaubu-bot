import json

data = []

file_name = input("File name: ")
# Files included:
# add dump/ if started from git root
# xkaubu_no_replies_1.json
# xkaubu_no_replies_2.json
# xkaubu_no_replies_3.json
# xkaubu_no_replies_4.json

with open(file_name) as f:
    data.append(json.load(f))

for item in data:
    print(f"item: {item}")
# After you run tweet_dumper_api.py and it serializes the data into a pickle file, run the file through here.

import pickle

# dump/xkaubu.pickle
file_path = input("Pickled file: ")

data = None

with open(file_path, "rb") as f:
    data = pickle.load(f, encoding="UTF8")

messages = []

for tweets in data:
    # messages.append(tweets.text)
    messages.append(f"{tweets.text}\n")

output_file = input("Output file: ")

with open(output_file, "w") as f:
    f.writelines(messages)
import json

with open("credentionals.json") as config_file:
    config = json.load(config_file)

OPEN_API_KEY = config["OPEN_API_KEY"]
PINECONE_API_KEY = config["PINECONE_API_KEY"]

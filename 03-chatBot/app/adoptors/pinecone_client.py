import os
from app.configs.constants import PINECONE_API_KEY
from pinecone import ServerlessSpec
from pinecone import Pinecone


# Replace SOME_CONSTANT with actual constants or import as needed
class PineconeClient:
    def __init__(self):
        self.pine_client = Pinecone(api_key=PINECONE_API_KEY)

    def create_index(self,index_name):
        if index_name not in self.pine_client.list_indexes().names():
            self.pine_client.create_index(
                name=index_name,
                dimension=2,
                metric="cosine",
                spec=ServerlessSpec(
                    cloud='aws',
                    region='us-east-1'
                )
            )
            print('Index created! : {}'.format(index_name))
        else:
            print(f'index name : {index_name} Index is already in Pinecone ')


if __name__ == '__main__':
    pinecone_client = PineconeClient()

import os
from dotenv import load_dotenv
from langchain_openai.chat_models import ChatOpenAI
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.llms import Ollama
from langchain_community.embeddings import OllamaEmbeddings


load_dotenv()

OPEN_API_KEY = os.getenv("OPEN_API_KEY")

class LLMModels:
    def __init__(self,
                 model_name=None):

        if model_name is not None:
            self.model_name = model_name
        else:
            self.model_name = "llama3.1:8b"


    def get_llm_model(self):

        if self.model_name.startswith('gpt'):
            model = ChatOpenAI(
                api_key=OPEN_API_KEY,
                model=self.model_name
            )
            embeddings = OpenAIEmbeddings(
                api_key=OPEN_API_KEY
            )
        else:
            model = Ollama(
                model=self.model_name
            )
            embeddings = OllamaEmbeddings(
                model=self.model_name
            )
        return model , embeddings


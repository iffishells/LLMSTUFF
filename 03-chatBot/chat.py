{
from utils import LLMModels

if __name__ == '__main__':
    sample_message = "Hello bruh! This is Monday, March 20."
given_models = {
    "1": "gpt-3.5-turbo",
    "2": "mixtral:8x7b",
    "3": "llama3.1:8b",
}
model_name = given_models['3']
llm_models = LLMModels(model_name=model_name)
model, embeddings = llm_models.get_llm_model()
print(model.invoke(sample_message))
}

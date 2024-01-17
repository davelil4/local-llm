from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline
from transformers import AutoTokenizer, AutoModelForCausalLM, AutoModelForSeq2SeqLM, pipeline
import os

class Models:
    models: dict = {}



# model_id = 'roneneldan/TinyStories-1M'

# model_name = model_id.split('/')[1]

# path = f'models/{model_name}'
# tokenizer = AutoTokenizer.from_pretrained(path)
# model = AutoModelForCausalLM.from_pretrained(path)

# pl = pipeline(
#     "text-generation",
#     model=model, 
#     tokenizer=tokenizer, 
#     max_length=128
# )

# local_llm = HuggingFacePipeline(pipeline=pl)

def create_llm(mn, typ):
    path = f'models/{typ}/{mn}'
    tokenizer = AutoTokenizer.from_pretrained(path)
    model = AutoModelForCausalLM.from_pretrained(path)

    pl = pipeline(
        "text-generation",
        model=model, 
        tokenizer=tokenizer, 
        max_length=128
    )

    local_llm = HuggingFacePipeline(pipeline=pl)

for m in os.listdir('models/tg'):
    Models.models[m] = create_llm(m, 'tg')

for m in os.listdir('models/t2g'):
    Models.models[m] = create_llm(m, 't2t')
# template = """Question: {question}

# Answer: Let's think step by step."""

# prompt = PromptTemplate(template=template, input_variables=["question"])

# llm_chain = LLMChain(prompt=prompt, 
#                      llm=local_llm
#                      )

def gen(text, model):
    return local_llm.invoke(text)

if __name__ == '__main__':
    print(local_llm.invoke("Where is istanbul?"))
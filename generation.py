from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline
from transformers import AutoTokenizer, AutoModelForCausalLM, AutoModelForSeq2SeqLM, pipeline
from langchain.prompts.prompt import PromptTemplate
from langchain.chains import LLMChain

model_id = 'google/flan-t5-small'

model_name = model_id.split('/')[1]

path = f'models/{model_name}'
tokenizer = AutoTokenizer.from_pretrained(path)
model = AutoModelForSeq2SeqLM.from_pretrained(path)

pl = pipeline(
    "text2text-generation",
    model=model, 
    tokenizer=tokenizer, 
    max_length=128
)

local_llm = HuggingFacePipeline(pipeline=pl)

# template = """Question: {question}

# Answer: Let's think step by step."""

# prompt = PromptTemplate(template=template, input_variables=["question"])

# llm_chain = LLMChain(prompt=prompt, 
#                      llm=local_llm
#                      )

if __name__ == '__main__':
    print(local_llm.invoke("Where is istanbul?"))
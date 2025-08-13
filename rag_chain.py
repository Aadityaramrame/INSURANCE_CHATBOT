# rag_chain.py

import os
from huggingface_hub import login
from dotenv import load_dotenv
from retriever import setup_vectorstore
from langchain.chains import RetrievalQA
from langchain_huggingface import HuggingFacePipeline 
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
import torch

# Load environment variables
load_dotenv()
hf_token = os.getenv("HF_TOKEN")

# Login
login(token=hf_token)

# Check GPU availability
device = 0 if torch.cuda.is_available() else -1
print(f"Using device: {'GPU' if device == 0 else 'CPU'}")

# Model config (optional: 4-bit to save VRAM)
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16
)

model_id = "mistralai/Mistral-7B-Instruct-v0.3"

# Load tokenizer & model
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    quantization_config=bnb_config,  # ✅ enable quantization
    device_map="auto"
)

# Hugging Face text generation pipeline
hf_pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=512,
    temperature=0.2,
    do_sample=True,
    device=device  # ✅ force GPU if available
)

# Wrap in LangChain
llm = HuggingFacePipeline(pipeline=hf_pipe)

# FAISS retriever
retriever = setup_vectorstore()

# RAG chain
rag_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True
)

def get_rag_response(query):
    result = rag_chain.invoke({"query": query})
    return result["result"]

if __name__ == "__main__":
    while True:
        query = input("Ask: ")
        if query.lower() in ["exit", "quit"]:
            break
        print(get_rag_response(query))

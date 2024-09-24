from langchain_cohere import Cohere
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up Cohere API key
os.environ["COHERE_API_KEY"] = os.getenv("COHERE_API_KEY")

# Prompt template
prompt = ChatPromptTemplate(
    [
        ("system", "you are a helpful assistant. please respond to the user queries"),
        ("user", "Question: {question}"),
    ]
)

# Streamlit app
st.title("LangChain Cohere Chatbot")
input_text = st.text_input("Search the topic you want")

# Initialize Cohere model
cohere_model = Cohere(model="command-xlarge-20221108")  # Replace with the desired model if different

output_parser = StrOutputParser()
chain = prompt | cohere_model | output_parser

if input_text:
    st.write(chain.invoke({'question': input_text}))

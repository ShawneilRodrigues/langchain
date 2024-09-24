from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langserve import add_routes
import uvicorn
import os
from cohere import Client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set Cohere API key
os.environ['COHERE_API_KEY'] = os.getenv("COHERE_API_KEY")
cohere_api_key = os.getenv("COHERE_API_KEY")

# Initialize FastAPI app
app = FastAPI(
    title="Langchain Server with Cohere",
    version="1.0",
    description="A simple API Server that integrates Cohere LLM"
)

# Initialize Cohere client
cohere_client = Client(cohere_api_key)

# Define prompts for Cohere
prompt1 = ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")
prompt2 = ChatPromptTemplate.from_template("Write me a poem about {topic} for a 5-year-old child with 100 words")

# Function to call Cohere API for text generation
def generate_text(prompt: str, topic: str):
    response = cohere_client.generate(
        model='command-r-plus-08-2024',  # Example Cohere model
        prompt=prompt.format(topic=topic),
        max_tokens=100  # Adjust as per requirement
    )
    return response.generations[0].text.strip()

# Add route for generating essay
@app.post("/essay")
async def generate_essay(topic: str):
    essay_prompt = prompt1.format(topic=topic)
    result = generate_text(essay_prompt, topic)
    return {"essay": result}

# Add route for generating poem
@app.post("/poem")
async def generate_poem(topic: str):
    poem_prompt = prompt2.format(topic=topic)
    result = generate_text(poem_prompt, topic)
    return {"poem": result}

# Run the FastAPI app
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8500)

import requests
import streamlit as st

# Function to get response from Cohere essay generation endpoint
def get_openai_response(input_text):
    response = requests.post(
        "http://localhost:8500/essay/invoke",  # Assuming this route is linked to Cohere for essay generation
        json={'topic': input_text}      # Sending the topic as expected by your FastAPI endpoint
    )
    if response.status_code == 200:
        try:
            return response.json()['essay']  # Adjusting based on the expected response structure
        except KeyError:
            st.error("Unexpected response structure.")
    else:
        st.error(f"API Error: {response.status_code} - {response.text}")

# Function to get response from Cohere poem generation endpoint
def get_ollama_response(input_text):
    response = requests.post(
        "http://localhost:8500/poem/invoke",  # Assuming this route is linked to Cohere for poem generation
        json={'topic': input_text}     # Sending the topic as expected by your FastAPI endpoint
    )
    if response.status_code == 200:
        try:
            return response.json()['poem']  # Adjusting based on the expected response structure
        except KeyError:
            st.error("Unexpected response structure.")
    else:
        st.error(f"API Error: {response.status_code} - {response.text}")

# Streamlit framework
st.title('Langchain Demo With Cohere API')

# Input fields for essay and poem topics
input_text = st.text_input("Write an essay on:")
input_text1 = st.text_input("Write a poem on:")

# Display the generated essay
if input_text:
    st.write(get_openai_response(input_text))

# Display the generated poem
if input_text1:
    st.write(get_ollama_response(input_text1))

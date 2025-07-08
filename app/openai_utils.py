import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

client = openai.OpenAI()

system_prompt = {"role": "system", "content": "You are a splunk expert assistant. Only respond to questions about splunk. Politely decline other topics. "}

def stream_openai_response(messages: list):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages= [system_prompt] + messages,
        stream=True
    )
    full_response = ""
    for chunk in response:
        if chunk.choices and chunk.choices[0].delta.content:
            delta = chunk.choices[0].delta.content
            full_response += delta
            yield full_response
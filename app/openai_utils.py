import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
openai_model = os.getenv("OPENAI_MODEL", "gpt-4o")

client = openai.OpenAI()

assistant_system_prompt = {"role": "system", "content": "You are an expert assistant that will translate a human textual request. Only respond to questions about splunk. Politely decline other topics. "}

splunk_engineer_system_prompt = {
    "role": "system",
    "content": """You are a senior Splunk engineer.

Here is the log schema you must use for all queries:
{
    "Host": "string",
    "Date": "string",
    "Thread": "string",
    "Identifiers": {
        "App-Name": "string",
        "Processor": "string",
        "Version": "string",
        "AuthzClientId": "string",
        "RequestDateTime": "string",
        "WalletId": "string",
        "ConversationId": "string",
        "CustomAttributes": {
            "AppEnv": "string"
        }
    },
    "Level": "string",
    "Logger": "string",
    "Msg": "string"
}

Rules:
- Use only fields from the schema above.
- Return ONLY the Splunk SPL query as plain text.
- Do not include explanations, comments, or any extra text.
- If time constraints are mentioned, use `earliest=` or `latest=`.
- Assume `index=main` unless specified otherwise."""
}

def stream_openai_response(messages: list):
    response = client.chat.completions.create(
        model=openai_model,
        messages= [assistant_system_prompt] + messages,
        stream=True
    )
    full_response = ""
    for chunk in response:
        if chunk.choices and chunk.choices[0].delta.content:
            full_response += chunk.choices[0].delta.content            
            yield full_response

def generate_splunk_spl_query(messages: list):
    messages = [splunk_engineer_system_prompt] + messages
    response = client.chat.completions.create(model=openai_model, messages=messages)
    yield response.choices[0].message.content.strip()

def summarize_results(results):
    system_prompt = {
        "role": "system",
        "content": "You are a data analyst. Summarize JSON data from Splunk for business users.\n"
                   "Be concise, non-technical, and suggest a chart type if visualization helps.\n"
                   "\n"
                   "Example:\n"
                   "Input: [{\"region\":\"US\",\"sales\":1200},{\"region\":\"EU\",\"sales\":800}]\n"
                   "Output: US contributed 60% of sales, EU 40%. Suggested chart: pie."
    }
    messages = [system_prompt, {"role": "user", "content": str(results)}]
    response = openai.ChatCompletion.create(model=openai_model, messages=messages)
    return response.choices[0].message.content.strip()
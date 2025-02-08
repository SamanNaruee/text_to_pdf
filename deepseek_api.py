"""
DeepSeek API Usage Examples:

Using cURL:

curl -X POST https://api.deepseek.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "model": "deepseek-chat",
    "messages": [
      {"role": "user", "content": "What is AI?"}
    ],
    "temperature": 0.7
  }'


Using Postman:
1. Create a new POST request to https://api.deepseek.com/v1/chat/completions
2. Add header: 
   - Key: Content-Type, Value: application/json
   - Key: Authorization, Value: Bearer YOUR_API_KEY
3. In Body tab, select raw and JSON, then add:
{
    "model": "deepseek-chat",
    "messages": [
        {"role": "user", "content": "What is AI?"}
    ],
    "temperature": 0.7
}

Using Python:

import requests

api_key = "YOUR_API_KEY"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

data = {
    "model": "deepseek-chat",
    "messages": [
        {"role": "user", "content": "What is AI?"}
    ],
    "temperature": 0.7
}

response = requests.post(
    "https://api.deepseek.com/v1/chat/completions",
    headers=headers,
    json=data
)

print(response.json())


Available Models:
- deepseek-chat: General purpose chat model
- deepseek-coder: Code-specific model

Common Parameters:
- temperature: Controls randomness (0.0 to 1.0)
- max_tokens: Maximum length of response
- top_p: Nucleus sampling parameter
- presence_penalty: Penalizes new tokens based on presence
- frequency_penalty: Penalizes new tokens based on frequency
"""


from openai import OpenAI

client = OpenAI(api_key="sk-4597e33be0eb4232a8df6bf1d58afb93", base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant that explains things as it can be explained, aslo you must mention details"
        },
        {"role": "user", "content": "Hello"},
    ],
    stream=False
)

print(response.choices[0].message.content)
from openai import OpenAI

client = OpenAI(
    base_url="https://api.aimlapi.com/v1",
    api_key="fb8e12ece56243059944ea9c26cdc42e",
)

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "system",
            "content": "You are an AI assistant who knows everything.",
        },
        {"role": "user", "content": "Tell me, why is the sky blue?"},
    ],
)

message = response.choices[0].message.content

print(f"Assistant: {message}")

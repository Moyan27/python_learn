from openai import OpenAI
client = OpenAI()
client.api_key="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"
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message)

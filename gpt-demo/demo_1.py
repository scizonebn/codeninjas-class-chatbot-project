from openai import OpenAI

client = OpenAI(
  api_key="api_key_here",
)

# A prompt to generate a short story
prompt_1 = '''
Write a short story about a young boy who finds a magical book in his school library. The book allows him to travel to different worlds.
'''

# Generating response back from gpt-3.5-turbo
openai_response = client.chat.completions.create(
    model = 'gpt-3.5-turbo',
    messages = [{'role': 'user', 'content': prompt_1}]
)

# print(openai_response)
print(openai_response.choices[0].message.content)
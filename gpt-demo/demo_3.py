# 1. Get API key from OpenAI
# 2. pip install openai

from openai import OpenAI

client = OpenAI(
  api_key="api_key_here",
)

# A list of Q&A pairs - You can train it to understand our own data, but you need additional tools to do that.
# qa_pairs = [
#     ("What is the capital of France?", "Paris"),
#     ("Who wrote 'Harry Potter'?", "J.K. Rowling"),
#     ("What is the largest planet in our solar system?", "Jupiter"),
# ]

# A prompt to create a simple Q&A chatbot
prompt_3 = '''
You are a friendly and helpful chatbot. Answer the following questions:

1. What is the capital of France?
2. Who wrote 'Harry Potter'?
3. What is the largest planet in our solar system?
'''

# Generating response back from gpt-3.5-turbo
openai_response = client.chat.completions.create(
    model = 'gpt-3.5-turbo',
    messages = [{'role': 'user', 'content': prompt_3}]
)

print(openai_response.choices[0].message.content)
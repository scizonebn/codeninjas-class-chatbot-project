# Explore GPT API

# Import the OpenAI library to use AI models
from openai import OpenAI

# Set up a client to talk to OpenAI's API using a secret key
client = OpenAI(
  api_key="api_key_here",  # This is your secret password for the AI!
)

# A prompt to generate a short story
prompt_1 = '''
Write a short story about a young boy who finds a magical book in his school library. The book allows him to travel to different worlds.
'''

# Ask the AI to create a story based on the prompt
openai_response = client.chat.completions.create(
    model='gpt-3.5-turbo',  # Use this version of the AI
    messages=[{'role': 'user', 'content': prompt_1}]  # Send the story idea to the AI
)

# Print the story created by the AI
print(openai_response.choices[0].message.content)

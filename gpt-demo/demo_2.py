# 1. Get API key from OpenAI
# 2. pip install openai

from openai import OpenAI

client = OpenAI(
  api_key="api_key_here",
)

# Text to summarize
text_to_summarize = '''
Dinosaurs were a diverse group of reptiles that appeared during the Triassic period, between 243 and 233 million years ago. They became the dominant terrestrial vertebrates after the Triassic–Jurassic extinction event 201 million years ago; their dominance continued through the Jurassic and Cretaceous periods. The fossil record shows that birds are feathered dinosaurs, having evolved from earlier theropods during the Late Jurassic period. As such, birds were the only dinosaur lineage to survive the Cretaceous–Paleogene extinction event approximately 66 million years ago.
'''

# A prompt to summarize the given text
prompt_2 = f'''
Please summarize the following text in simple terms suitable for a 12-year-old upto 25 word count:

{text_to_summarize}
'''

# Generating response back from gpt-3.5-turbo
openai_response = client.chat.completions.create(
    model = 'gpt-3.5-turbo',
    messages = [{'role': 'user', 'content': prompt_2}]
)

print(openai_response.choices[0].message.content)
import os
from openai import OpenAI


def send_to_llm(prompt, model="llama3"):
    if model in ("gpt-4o", "gpt-4-turbo-preview", "gpt-3.5-turbo"):
        api_key = os.environ["OPENAI_API_KEY"]
        client = OpenAI(api_key=api_key)
    else:
        client = OpenAI(
            base_url='http://localhost:11434/v1',
            api_key='ollama',  # required, but unused
        )

    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "system", "content": prompt}],
        temperature=0.7,
        max_tokens=1000,
        top_p=0.8,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )

    return response.choices[0].message.content

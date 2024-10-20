from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)


def generate_text(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.8,
            top_p=0.0,
            frequency_penalty=0,
            presence_penalty=0,
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"An error occurred generate_text: {e}")
        raise e

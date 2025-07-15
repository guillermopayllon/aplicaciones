import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def analizar_error(error_input):
    prompt = f"""
    Actúa como un asistente técnico experto.
    Analiza el siguiente mensaje de error y proporciona:
    1. Una explicación clara para principiantes.
    2. Las 3 causas más probables.
    3. Soluciones prácticas.

    Error:
    {error_input}
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

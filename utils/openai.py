from openai import OpenAI
from utils.env import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def get_recepy_openai(words):

    prompt = f"Genera una receta utilizando los siguientes ingredientes: {words}. "\
    "Si el usuario tiene alguna preferencia, como ser vegetariano, sin gluten, o bajo en calorías, ajusta la receta para cumplir con esos criterios. Asegúrate de proporcionar los pasos de preparación detallados y sugerir opciones de ingredientes sustitutos si es necesario. Tratá de no agregar ingredientes que no sean los que el usuario ingreso de ser posible."

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user",
            "content": prompt}
        ]
    )

    return completion.choices[0].message.content

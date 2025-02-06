import google.generativeai as genai
from utils.env import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

def get_recepy_gemini(words):
    
    prompt = f"Genera una receta utilizando los siguientes ingredientes: {words}. "\
    "Si el usuario tiene alguna preferencia, como ser vegetariano, sin gluten, o bajo en calorías, ajusta la receta para cumplir con esos criterios. Asegúrate de proporcionar los pasos de preparación detallados y sugerir opciones de ingredientes sustitutos si es necesario. Tratá de no agregar ingredientes que no sean los que el usuario ingreso de ser posible."
    
    model = genai.GenerativeModel("gemini-1.5-flash")
    completion = model.generate_content(prompt)

    return completion.text



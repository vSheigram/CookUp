import streamlit as st
from utils.main import get_recepy

st.title("CookUp")

st.html("""
    <hr>
    <h2>Generador de Recetas</h2>
    <ol>
        <li>Ingresa los ingredientes que tenés en tu casa para que te genere una receta.</li>
        <li>Selecciona las preferencias dietéticas que tenés.</li>
        <li>Haz click en el botón "Generar receta" y listo!</li>
    </ol>
""")

# Input de ingredientes
words = st.text_input("Ingresa los ingredientes separados por comas", 
                    "pan, leche, huevo, azúcar.")

# Casillas para preferencias dietéticas
vegan = st.checkbox('Vegano')
vegetarian = st.checkbox('Vegetariano')
celiac = st.checkbox('Celiaco')
low_calories = st.checkbox('Bajo en calorías')

# Crear una lista de preferencias basadas en lo que el usuario marque
preferences = []

if vegan:
    preferences.append("vegano")
if vegetarian:
    preferences.append("vegetariano")
if celiac:
    preferences.append("sin gluten")
if low_calories:
    preferences.append("bajo en calorías")

# Generar el mensaje para la IA
if len(preferences) > 0:
    preferences_text = " El usuario tiene las siguientes preferencias: " + ", ".join(preferences) + "."
else:
    preferences_text = " No hay preferencias especiales."

# Botón para generar la receta
if st.button("Generar receta"):
    full_input = words + preferences_text  # Incluir las preferencias en el input para la IA
    recepy = get_recepy(full_input)  # Llamar a la función con el texto completo
    st.write(recepy)

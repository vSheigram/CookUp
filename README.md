# CookUp - Generador de Recetas con IA

**CookUp** es una aplicación web que genera recetas personalizadas utilizando inteligencia artificial. Los usuarios ingresan los ingredientes que tienen disponibles y la aplicación, usando **OpenAI GPT-4**, sugiere recetas adaptadas a las preferencias alimenticias.

## Funcionalidad

1. **Ingreso de Ingredientes**: Los usuarios ingresan los ingredientes que tienen disponibles en su hogar.
2. **Preferencias Dietéticas**: Los usuarios pueden seleccionar preferencias como "Vegano", "Vegetariano", "Sin Gluten" o "Bajo en Calorías".
3. **Generación de Recetas**: La IA genera recetas basadas en los ingredientes y preferencias ingresados, proporcionando pasos detallados y alternativas para sustitutos.

## Requisitos

- Python 3.x
- Streamlit
- OpenAI API Key (GPT-4)

## Instalación

1. Clona el repositorio:
  ```bash
  git clone https://github.com/vSheigram/CookUp.git
  ```
2. Instala las dependencias:
  ```bash
  pip install -r requirements.txt
  ```
3. Crea un archivo .env y agrega las claves de API para OpenAI y Gemini:

Crea el archivo .env en la raíz del proyecto con el siguiente contenido:
  ```bash
  OPENAI_API_KEY=tu_openai_api_key_aqui
  GEMINI_API_KEY=tu_gemini_api_key_aqui
  TYPE_AI=gemini  # Cambia 'gemini' por 'openai' para usar OpenAI GPT-4o-mini
  ```
## Explicación del archivo `.env`:

- **OPENAI_API_KEY**: Tu clave de API para **OpenAI**.
- **GEMINI_API_KEY**: Tu clave de API para **Gemini**.
- **TYPE_AI**: Define qué IA utilizar. Puedes configurarlo como:
  - `"gemini"` para usar **Google Gemini**.
  - `"openai"` para usar **OpenAI GPT-4o-mini**.

4. Ejecuta la aplicación:
  ```bash
  streamlit run app.py
  ```

## Uso

1. Abre la aplicación en tu navegador.
2. Ingresa los ingredientes que tienes disponibles.
3. Selecciona las preferencias dietéticas si las tienes.
4. Haz clic en "Generar receta" para obtener una receta personalizada.


## Enlaces

- [Aplicación en Streamlit](https://cookup-tp-final.streamlit.app/)
- [Repositorio en GitHub](https://github.com/vSheigram/CookUp)

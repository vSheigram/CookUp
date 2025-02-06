from utils.env import TYPE_AI
from utils.openai import get_recepy_openai
from utils.gemini import get_recepy_gemini

def get_recepy(words):
    if TYPE_AI == "openai":
        return get_recepy_openai(words)
    elif TYPE_AI == "gemini":
        return get_recepy_gemini(words)


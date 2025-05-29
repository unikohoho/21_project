from openai import OpenAI
import os

def load_openai_api_key(filepath="keys/openai_key.txt"):
    with open(filepath, "r") as file:
        return file.read().strip()

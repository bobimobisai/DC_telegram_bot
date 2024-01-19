from dotenv import load_dotenv
import os


def get_token(type: str):
    load_dotenv()
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    GPT_TOKEN = os.getenv("GPT_TOKEN")
    if type == "BOT":
        return BOT_TOKEN
    else:
        return GPT_TOKEN

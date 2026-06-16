from dotenv import load_dotenv
import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI

from pydantic import BaseModel, Field
from typing import Literal

load_dotenv('api_keys.env')

GITHUB_PAT = os.getenv('GITHUB_PAT')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

GITHUB_URL = os.getenv('GITHUB_URL')

GPT_MODEL = os.getenv('GPT_MODEL')
GEMINI_MODEL = os.getenv('GEMINI_MODEL')

main_model = ChatGoogleGenerativeAI(
    model=GEMINI_MODEL,
    api_key=GEMINI_API_KEY,
    temperature=0.1,
    max_retries=2
)

sub_model = ChatOpenAI(
    model=GPT_MODEL,
    api_key=GITHUB_PAT,
    base_url=GITHUB_URL,
    max_retries=5
)

class structured_out(BaseModel):
    name: Literal['me', 'you'] = Field(description='Кто сейчас отвечает.')
    res: str = Field(description='Почему ты так решил')
    
s_model = main_model.with_structured_output(structured_out)
response = s_model.invoke('Привет, ответь, кто ответит')

print(response)

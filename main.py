from fastapi import FastAPI
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

@app.get("/")
def read_root():
    greeting_from_env = os.getenv("FASTAPI_GREETING", "Default FastAPI Greeting")
    return {"message": f"Hello FastAPI! {greeting_from_env}"}
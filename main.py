from fastapi import FastAPI
import os
from dotenv import load_dotenv

# 1. Get the environment from a variable, e.g., 'development', 'staging', 'production'
# This variable will be set by Docker Compose at runtime. Defaults to 'development'.
APP_ENV = os.getenv("APP_ENV", "dev")

# 2. Construct the .env filename, e.g., '.env.development'
dotenv_path = f".env.{APP_ENV}"

# 3. Load the specific .env file
# The load_dotenv function will gracefully handle cases where the file doesn't exist.
load_dotenv(dotenv_path=dotenv_path)

# Now, the rest of the app can use os.getenv() for all other variables.
# These variables could be from the loaded file or already present in the environment.
GREETING = os.getenv("FASTAPI_GREETING", "Default FastAPI Greeting")

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": f"Hello FastAPI!", "greeting": GREETING, "environment": APP_ENV}
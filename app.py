## Imports pythons built in os module. Allows program to read enviroment variables, including the OPENAI_API_KEY
import os
##imports load_dotnev function from python-dotnev package we installed
from dotenv import load_dotenv

load_dotenv() ## Finds the .env file and loads its variables into the programs env
## Looks for env variable named OPENAI_API_KEY and stores its value inside api_key
## If it can not find the var, api_key will be set to None.
api_key = os.getenv("OPENAI_API_KEY") 

if api_key:
    print("API key loaded successfully.")
else:
    print("Failed to load API key.")
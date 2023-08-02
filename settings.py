import os
from dotenv import load_dotenv

load_dotenv()

EVENT_CODE = "XXMel"
USERNAME = os.getenv("FMSUSERNAME")
TOKEN = os.getenv("FMSTOKEN")
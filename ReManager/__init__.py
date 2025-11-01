import logging
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(format="[ReManger-Backend] %(name)s: %(message)s",handlers=[logging.FileHandler("ReManager-Backend.log"), logging.StreamHandler()],level=logging.INFO)
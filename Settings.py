import os

from dotenv import load_dotenv

load_dotenv()
ENABLE_DOCS = os.getenv("ENABLE_DOCS", 'True').lower() in ('true', '1', 't')
RUN_MODE = os.getenv("RUN_MODE", "beast")
MAX_HEIGHT = int(os.getenv("MAX_HEIGHT", 3000))
MAX_WIDTH = int(os.getenv("MAX_WIDTH", 3000))
MAX_DPI = int(os.getenv("MAX_DPI", 600))

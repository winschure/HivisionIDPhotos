import os

from dotenv import load_dotenv

load_dotenv()
ENABLE_DOCS = os.getenv("ENABLE_DOCS", 'True').lower() in ('true', '1', 't')
RUN_MODE = os.getenv("RUN_MODE", "beast")
from os import environ
from dotenv import load_dotenv

load_dotenv(verbose=True)

OPENAI_API_KEY = environ.get("OPENAI_API_KEY")

SUPABASE_URL = environ.get("SUPABASE_URL")
SUPABASE_ANON_KEY = environ.get("SUPABASE_ANON_KEY")

MAX_PUSH_EVENT_FILE_COUNT = int(environ.get("MAX_PUSH_EVENT_FILE_COUNT", 20))

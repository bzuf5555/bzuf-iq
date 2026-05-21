import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN: str = os.getenv("BOT_TOKEN", "")
MONGO_URI: str = os.getenv("MONGO_URI", "")
WEBHOOK_URL: str = os.getenv("WEBHOOK_URL", "")
PORT: int = int(os.getenv("PORT", "8443"))
DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"

WEBHOOK_PATH = "/webhook"
HEALTH_PATH = "/health"

DB_NAME = "bzuf_iq"
USERS_COLLECTION = "users"
RESULTS_COLLECTION = "test_results"

TOTAL_QUESTIONS = 20

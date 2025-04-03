import os
from google.cloud import storage
from dotenv import load_dotenv
import json
from google.oauth2 import service_account

# Load .env for local development only
load_dotenv()

# Tokens and keys from environment
TOKEN = os.getenv("BOT_TOKEN")
DB_CONNECTION_STRING = os.getenv("DB_CONNECTION_STRING")
GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")
BUCKET_NAME = os.getenv("BUCKET_NAME")

# Determine whether running in Azure (JSON string) or local (file)
if os.getenv("GOOGLE_CREDENTIALS_JSON"):
    # Azure: credentials stored as JSON string in environment variable
    creds_json = os.getenv("GOOGLE_CREDENTIALS_JSON")
    creds_dict = json.loads(creds_json)
    credentials = service_account.Credentials.from_service_account_info(creds_dict)
    storage_client = storage.Client(credentials=credentials)
else:
    # Local: credentials stored in gcloud_key.json file
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "gcloud_key.json"
    storage_client = storage.Client()

# Init the GCS bucket
bucket = storage_client.bucket(BUCKET_NAME)

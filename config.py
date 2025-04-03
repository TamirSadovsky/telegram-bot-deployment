import os
from google.cloud import storage
from dotenv import load_dotenv
import json
from google.oauth2 import service_account
load_dotenv()


TOKEN = os.getenv("BOT_TOKEN")

DB_CONNECTION_STRING = os.getenv("DB_CONNECTION_STRING")

GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")
BUCKET_NAME = os.getenv("BUCKET_NAME")

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
storage_client = storage.Client()
bucket = storage_client.bucket(BUCKET_NAME)


# ✅ Initialize Google Cloud Storage client
storage_client = storage.Client()
bucket = storage_client.bucket(BUCKET_NAME)


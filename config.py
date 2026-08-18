import os


API_ID = int(os.getenv("API_ID", "1234567")) 
API_HASH = os.getenv("API_HASH", "your_api_hash_here") 
BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token_here")  
MONGO_DB_URI = os.getenv("MONGO_DB_URI", "your_mongodb_uri_here")


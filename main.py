# main.py

import logging
from pyrogram import Client
import config


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


app = Client(
    "ManagementBot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    plugins=dict(root="tg_bot")
)

if __name__ == "__main__":
    logger.info("🤖 Bot စတင်အလုပ်လုပ်နေပါပြီ...")
    app.run()

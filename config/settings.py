import os
import json
from dotenv import load_dotenv

load_dotenv()

# ギフトコード
GIFT_PATH = "config/gift.json"
with open(GIFT_PATH) as f:
    GIFT_DATA = json.load(f)
GIFT_DATA['player_ids'] = os.getenv('PLAYER_IDS').split(',')

# ぽちぽち
POTI_PATH = "config/poti.json"
with open(POTI_PATH) as f:
    POTI_DATA = json.load(f)

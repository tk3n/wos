import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import settings

gift_data = settings.GIFT_DATA

EXCHANGE_CENTER_URL = gift_data['exchange_center_url']
GIFT_CODES = gift_data['gift_codes']
PLAYER_IDS = gift_data['player_ids']
TIME_OUT = gift_data['time_out']

def exchange_gift_code(driver, player_id, gift_code):
    # ページ上のすべての要素が読み込まれるまで待機
    driver.get(EXCHANGE_CENTER_URL)
    WebDriverWait(driver, TIME_OUT).until(EC.presence_of_all_elements_located)

    # プレイヤーIDの入力欄を見つけて値を入力
    player_id_field = driver.find_element(By.XPATH, "//input[@placeholder='プレイヤーID']")
    player_id_field.send_keys(player_id)

    # ログインボタンをクリック
    login_button = driver.find_element(By.CSS_SELECTOR, "div.login_btn")
    login_button.click()

    time.sleep(1)

    # ギフトコードの入力欄を見つけて値を入力
    gift_code_field = driver.find_element(By.XPATH, "//input[@placeholder='交換コードを入力してください']")
    gift_code_field.send_keys(gift_code)

    # 交換ボタンをクリック
    exchange_button = driver.find_element(By.CSS_SELECTOR, "div.exchange_btn")
    exchange_button.click()

    time.sleep(1)

driver = webdriver.Chrome()
try:
    for player_id in PLAYER_IDS:
        for gift_code in GIFT_CODES:
            exchange_gift_code(driver, player_id, gift_code)

except Exception as e:
        print(f"予期せぬエラーが発生しました: {str(e)}")

finally:
    driver.quit()

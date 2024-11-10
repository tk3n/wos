import time
import random
import pyautogui
from pynput import keyboard
from config import settings

poti_data = settings.POTI_DATA

# ばらけさせるパターン
PATTERNS = poti_data['patterns']
WIDTH_RANGE = poti_data['width_range']
HEIGHT_RANGE = poti_data['height_range']

# ポチる間隔
POTI_INTERVAL = poti_data['poti_interval']

# ポチる場所
DEFAULT_PLACES = poti_data['default_places']

def generate_random_patterns(DEFAULT_PLACES, num_patterns=PATTERNS):
    patterns = []
    for _ in range(num_patterns):
        pattern = []
        for place in DEFAULT_PLACES:
            x = place[0] + random.randint(-WIDTH_RANGE, WIDTH_RANGE)
            y = place[1] + random.randint(-HEIGHT_RANGE, HEIGHT_RANGE)
            pattern.append([x, y])
        patterns.append(pattern)
    return patterns

random_patterns = generate_random_patterns(DEFAULT_PLACES)

# random_patterns = [[[place[0] + random.randint(-WIDTH_RANGE, WIDTH_RANGE), place[1] + random.randint(-HEIGHT_RANGE, HEIGHT_RANGE)] for place in DEFAULT_PLACES] for _ in range(PATTERNS)]

# escのフラグ
is_esc_pressed = False

# escが押されたらフラグを立ててFalseを返す
def on_press(key):
    global is_esc_pressed
    if key == keyboard.Key.esc:
        is_esc_pressed = True
        return False

# キー入力を監視
listener = keyboard.Listener(on_press=on_press)
listener.start()

# 0.1秒ごとにひたすらポチポチ
pattern_index = 0
while not is_esc_pressed:
    current_pattern = random_patterns[pattern_index % PATTERNS]
    for place in current_pattern:
        pyautogui.click(place[0], place[1])
    
    time.sleep(POTI_INTERVAL)
    pattern_index += 1

# 監視ストップ
listener.stop()
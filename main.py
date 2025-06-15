import pyautogui
import time
import pyperclip
from openai import OpenAI

# key = "your openai key"

# Step 1: Drag to select message
time.sleep(1)
pyautogui.moveTo(1015, 305, duration=0.3)
pyautogui.mouseDown()
pyautogui.moveTo(1020, 1200, duration=0.6)
pyautogui.mouseUp()

# Step 2: Copy the selected text
time.sleep(1)
pyautogui.hotkey('ctrl', 'c')
time.sleep(1)

# Step 3: Get text from clipboard
copied_text = pyperclip.paste()
print("Copied text:\n", copied_text)

# Step 4: Deselect by clicking outside
pyautogui.moveTo(1000, 281)
pyautogui.click()

# Step 5: Query OpenAI with message
client = OpenAI(api_key=key)

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a person named Manik who speaks Hindi as well as English. He is from India and is a coder. You analyze chat history and respond like Manik."},
        {"role": "user", "content": copied_text}
    ]
)

reply = response.choices[0].message.content
print("Reply:\n", reply)

# Step 6: Paste reply into WhatsApp and send
pyperclip.copy(reply)
time.sleep(0.5)
pyautogui.moveTo(1530, 950)
pyautogui.click()
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.3)
pyautogui.press('enter')

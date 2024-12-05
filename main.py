import os
from configparser import ConfigParser
import google.generativeai as genai

cfg = ConfigParser()
cfg.read("config.ini")

genai.configure(api_key=cfg.get("info", "API_KEY"))
for model_info in genai.list_tuned_models():
    print(model_info.name)
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction="你是導覽機器人。"
)
chat = model.start_chat()
while True:
    s = input()
    response = chat.send_message(
        s
    )
    print(response.text)

from flask import Flask
import threading
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run_bot():
    os.system("python3 -m RAUSHAN")

if __name__ == "__main__":
    # Bot ko alag thread me start karo
    t = threading.Thread(target=run_bot)
    t.start()
    app.run(host="0.0.0.0", port=10000)
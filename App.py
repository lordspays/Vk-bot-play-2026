from flask import Flask, request
import json

app = Flask(__name__)

CONFIRMATION_CODE = "e4fb8b24"  # ваш код из ВК

@app.route('/')
def home():
    return f"""
    <h1>🎮 VK BOT READY</h1>
    <p>Confirmation code: <strong>{CONFIRMATION_CODE}</strong></p>
    <p>URL для ВК: https://ваш-домен.vercel.app/callback</p>
    """

@app.route('/callback', methods=['POST'])
def callback():
    data = request.json
    print("Получен запрос:", data)
    
    if data.get('type') == 'confirmation':
        return CONFIRMATION_CODE
    
    return 'ok'

if __name__ == '__main__':
    app.run()

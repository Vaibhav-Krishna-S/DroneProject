import requests
import tempfile
import cv2

BOT_TOKEN = '8185533511:AAEv6gQGUz9qwtUzq3aq62AZ_zmRakbgJnU'  # Replace with your token
CHAT_ID = '7549353989'  # Replace with your chat/user ID

def send_telegram_alert(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        'chat_id': CHAT_ID,
        'text': message
    }

    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print("✅ Alert sent successfully!")
        else:
            print("❌ Failed to send alert:", response.text)
    except Exception as e:
        print("⚠️ Error sending alert:", e)


def send_telegram_image_alert(image, caption):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"

    with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as temp:
        cv2.imwrite(temp.name, image)
        with open(temp.name, 'rb') as photo:
            files = {'photo': photo}
            data = {'chat_id': CHAT_ID, 'caption': caption}
            response = requests.post(url, data=data, files=files)

    if response.status_code == 200:
        print("📸 Image alert sent!")
    else:
        print("❌ Failed to send image alert:", response.text)

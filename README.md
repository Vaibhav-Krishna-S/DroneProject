# DroneProject
A Streamlit-based real-time surveillance system that uses **YOLOv8** to detect people in drone or CCTV footage and sends alerts via **Telegram**.
# 🚨 Real-Time Intrusion Detection System using YOLOv8

This is an AI-based Intrusion Detection System built with **YOLOv8** and **Streamlit**. The system detects people/weapons in uploaded videos or live streams, and sends real-time alerts via **Telegram** and **Email (Mailjet)**.

---

## 🔍 Features

- ✅ **YOLOv8**-based object detection (weapons/people)
- 📂 Upload video files for offline processing
- 📹 Real-time camera stream processing
- 📬 Instant **Telegram** text + image alerts
- 📧 **Email alerts** via Mailjet
- 🧠 Alert **cooldown logic** to avoid spam
- 🖥️ Intuitive **Streamlit interface**
- 🎞️ Saves processed video with bounding boxes

---

## 🛠️ Tech Stack

- Python 3.8+
- Streamlit
- OpenCV
- YOLOv8 (Ultralytics)
- Telegram Bot API
- Mailjet API

---

## 📁 Folder Structure

streamlit_drone_model/
├── app.py # Streamlit UI
├── alerts.py # Alert logic (Telegram, Mailjet)
├── video_processing.py # Core video analysis logic
├── yolo_utils.py # YOLOv8 loading and inference
├── models/
│ └── weapon_detector.pt # Your trained YOLOv8 model
├── static/
│ └── output.mp4 # Output video with detections
├── requirements.txt
└── README.md


---

## 🚀 Setup Instructions

### 1. Clone the Repo


git clone https://github.com/yourusername/streamlit_drone_model.git
cd streamlit_drone_model

### 2. Install the Requirements
pip install -r requirements.txt

### 3. 🔐 Setup Telegram Alerts
- Talk to BotFather and create a bot.

- Get your BOT_TOKEN.

- Start a chat with the bot and note the CHAT_ID.

- Paste these in alerts.py:
  TELEGRAM_BOT_TOKEN = "your_token"
  TELEGRAM_CHAT_ID = "your_chat_id"

## optional: Setup Mailjet Email Alerts
- Create a Mailjet account.

- Go to Account > API Keys and generate keys.

- Paste them in alerts.py:
  MAILJET_API_KEY = "your_api_key"
  MAILJET_API_SECRET = "your_api_secret"
  SENDER_EMAIL = "your@mail.com"

### 3. Run the App:
  streamlit run app.py
  Upload a video OR

  - Start your webcam stream (press 'q' to quit)

  - View real-time alerts & processed results


### 💡 Future Ideas
Add audio alert tones

Heatmap of intrusions

Web-based dashboard

Multi-camera support

Save detection logs


### Working Video Link: https://drive.google.com/file/d/1omhII0bl43_iEeDAUIEhwf3ymhU_Ho-U/view?usp=sharing 

🧑‍💻 Author
Vaibhav Krishna S
IEEE Student Member | AI & ML Enthusiast
🔗 LinkedIn







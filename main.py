# main.py
import streamlit as st
import os
from utils.video_processing import process_video, process_stream
from utils.alerts import send_telegram_alert

# 🌐 Streamlit UI
st.set_page_config(page_title="Drone Intrusion Detection", layout="centered")
st.title("🚁 Intrusion Detection System")
st.write("Detect people in drone/CCTV footage and send alerts.")

# 📁 Video Upload Section
st.subheader("1️⃣ Upload a Video File")
video_file = st.file_uploader("Upload a video", type=["mp4", "avi", "mov"])

if video_file:
    with open("input_video.mp4", "wb") as f:
        f.write(video_file.read())

    st.info("🔄 Processing uploaded video...")

    result_path, intrusions = process_video("input_video.mp4")

    if result_path and os.path.exists(result_path) and os.path.getsize(result_path) > 0:
        st.success("✅ Video processed successfully!")

        # Show video
        with open(result_path, 'rb') as video_file:
            video_bytes = video_file.read()
            st.video(video_bytes)

        st.write(f"**🔍 Intrusions Detected:** `{intrusions}`")

        if intrusions > 0:
            send_telegram_alert(f"🚨 Intrusion detected in drone footage! Count: {intrusions}")
    else:
        st.error("❌ Failed to process the video.")

st.markdown("---")

# 📡 Live Stream Section
st.subheader("2️⃣ Live Camera Stream")

use_live = st.checkbox("Use webcam (or IP camera) for live monitoring")

if use_live:
    cam_source = st.text_input("Enter IP Camera URL (leave blank for webcam)", "")
    if st.button("▶️ Start Live Stream"):
        if cam_source.strip() == "":
            process_stream(source=0)  # Uses your computer's webcam
        else:
            process_stream(source=cam_source.strip())


import cv2
from .yolo_utils import load_model, detect_intrusions
from .alerts import send_telegram_alert, send_telegram_image_alert

def process_video(video_path):
    cap = cv2.VideoCapture(video_path)
    ret, frame = cap.read()

    if not ret:
        return None, 0

    height, width = frame.shape[:2]
    fps = cap.get(cv2.CAP_PROP_FPS)

    output_path = "output.mp4"
    fourcc = cv2.VideoWriter_fourcc(*'avc1')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    model = load_model()
    total_intrusions = 0

    cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        intrusions, processed_frame, intruder_images = detect_intrusions(frame, model)
        total_intrusions += intrusions

        if intrusions > 0:
            send_telegram_alert(f"🚨 Intrusion detected in video! Count: {intrusions}")
            for idx, img in enumerate(intruder_images):
                send_telegram_image_alert(img, f"🎯 Intruder #{idx+1}")

        out.write(processed_frame)

    cap.release()
    out.release()

    return output_path, total_intrusions


def process_stream(source=0):
    cap = cv2.VideoCapture(source)
    model = load_model()
    intrusion_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        intrusions, processed_frame, intruder_images = detect_intrusions(frame, model)
        intrusion_count += intrusions

        cv2.imshow("Live Stream - Press 'q' to quit", processed_frame)

        if intrusions > 0:
            send_telegram_alert(f"🚨 Intrusion detected in live stream! Count: {intrusions}")
            for idx, img in enumerate(intruder_images):
                send_telegram_image_alert(img, f"🎯 Live Intruder #{idx+1}")

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

from ultralytics import YOLO
import cv2

def load_model():
    return YOLO('yolov8n.pt')  # or your custom model path

def detect_intrusions(frame, model):
    results = model(frame)[0]
    intrusion_count = 0
    intruder_images = []

    for box in results.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        cls_id = int(box.cls[0])
        confidence = float(box.conf[0])

        if model.names[cls_id] == "person":
            intrusion_count += 1
            crop = frame[y1:y2, x1:x2]
            intruder_images.append(crop)

        label = f"{model.names[cls_id]} {confidence:.2f}"
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, label, (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    return intrusion_count, frame, intruder_images

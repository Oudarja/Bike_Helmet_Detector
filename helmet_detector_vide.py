import cv2
import math
import cvzone
from ultralytics import YOLO
import time
# Initialize video capture
video_path = "/media/tanmoy002/HDD/Bike_helmet_detector/traffic/NVR_ch1_main_20260330000000_20260330235960.dav"
cap = cv2.VideoCapture(video_path)

# Get video properties for output
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Video writer to save output
# out = cv2.VideoWriter("output_video.mp4",
#                       cv2.VideoWriter_fourcc(*'mp4v'),
#                       fps,
#                       (frame_width, frame_height))

# Load YOLO model
model = YOLO("Weights/helmet.pt")

# Define class names
classNames = ['With Helmet', 'Without Helmet']

# Set minimum confidence threshold
CONF_THRESHOLD = 0.5  # Only show detections with 50% confidence or higher
while True:
    success, img = cap.read()
    if not success:
        break

    results = model(img, stream=True)
    for r in results:
        boxes = r.boxes
        for box in boxes:
            conf = float(box.conf[0])
            if conf < CONF_THRESHOLD:
                continue

            x1, y1, x2, y2 = map(int, box.xyxy[0])
            w, h = x2 - x1, y2 - y1

            cvzone.cornerRect(img, (x1, y1, w, h))
            cls = int(box.cls[0])
            conf_rounded = math.ceil(conf * 100) / 100

            cvzone.putTextRect(
                img,
                f'{classNames[cls]} {conf_rounded}',
                (max(0, x1), max(35, y1)),
                scale=1,
                thickness=1
            )

    # ✅ SHOW VIDEO
    cv2.imshow("Output", img)
    time.sleep(0.04)  # ~30 FPS → increase for slower (e.g., 0.1)

    # ✅ SAVE VIDEO
    # out.write(img)

    # ✅ PRESS ESC TO EXIT
    if cv2.waitKey(1) & 0xFF == 27:
        break
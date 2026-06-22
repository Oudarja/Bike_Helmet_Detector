import cv2
import math
import cvzone
from ultralytics import YOLO

# Load YOLO model with custom weights
yolo_model = YOLO("Weights/best.pt")

# Define class names
class_labels = ['With Helmet', 'Without Helmet']

# Load the image
image_path = "YOLO_Helmet_Detection_Sample_Images/riders_1.jpg"
img = cv2.imread(image_path)

# Perform object detection
results = yolo_model(img)

# Loop through the detections and draw bounding boxes
for r in results:
    # r.boxes contains all bounding boxes detected in that frame.
    boxes = r.boxes
    for box in boxes:
        '''
        box.xyxy gives coordinates of the bounding box:
        (x1, y1) → top-left corner
        (x2, y2) → bottom-right corner
        '''
        x1, y1, x2, y2 = box.xyxy[0]
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

        w, h = x2 - x1, y2 - y1
        cvzone.cornerRect(img, (x1, y1, w, h))
        conf = math.ceil((box.conf[0] * 100)) / 100
        # box.cls[0] → predicted class index (e.g., 0 = helmet, 1 = person)
        cls = int(box.cls[0])

        if conf > 0.1:
            cvzone.putTextRect(img, f'{class_labels[cls]} {conf}', (x1, y1 - 10), scale=0.8, thickness=1, colorR=(255, 0, 0))

# Display the image with detections
cv2.imshow("Image", img)

# Close window when 'q' button is pressed
while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cv2.waitKey(1)
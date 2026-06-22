### Bike Helmet Detector
#### Overview

Bike Helmet Detector is a computer vision–based traffic monitoring system developed to automatically detect motorcycle riders and determine whether they are wearing helmets. 
The project utilizes the YOLOv8 object detection framework along with OpenCV to process images and videos for helmet compliance monitoring.

The system can be applied in:
  - Traffic surveillance
  - Smart city monitoring
  - Road safety enforcement
  - Automated violation detection
  - Research and educational projects

Features
- Helmet and No-Helmet detection
- YOLOv8-based object detection
- Video processing support
- Image inference support
- Custom-trained helmet detection model
- Dataset preparation utilities
- SORT tracking integration
- Bounding box visualization using OpenCV
- Exportable trained weights

```
Bike_helmet_detector/
│
├── Helmet Detector.v1i.yolov8/
│   ├── train/
│   │   ├── images/
│   │   └── labels/
│   │
│   ├── valid/
│   │   ├── images/
│   │   └── labels/
│   │
│   ├── test/
│   │   ├── images/
│   │   └── labels/
│   │
│   ├── data.yaml
│   ├── README.dataset.txt
│   └── README.roboflow.txt
│
├── Masked_face/
│   ├── images/
│   └── labels_coco/
│
├── Weights/
│   └── helmet.pt
│
├── sort/
│
├── output/
│   ├── images/
│   └── labels/
│
├── runs/
│   └── detect/
│       └── train/
│
├── YOLO_Helmet_Detection_Sample_Images/
│
├── helmet_detector.py
├── helmet_detector_vide.py
├── Make_dataset.py
├── make_all_txt_empty.py
├── sort.py
├── req.txt
└── .gitignore
```
### Module Description

#### helmet_detector.py
Image-based helmet detection module.

#### Responsibilities
- Load trained YOLOv8 helmet model
- Read input images
- Perform helmet detection
- Draw bounding boxes
- Display detection results
#### Output
- Detected riders with helmet status
- Annotated images

#### helmet_detector_vide.py
Video processing module.

Responsibilities
- Load video stream
- Read frames sequentially
- Run YOLO inference on each frame
- Detect helmet and no-helmet riders
- Draw detections on video frames
- Display processed video
 
#### Classes Detected
['With Helmet', 'Without Helmet']

#### Output
- Real-time helmet detection visualization
- Processed video stream

#### Make_dataset.py

Dataset preparation utility.

#### Responsibilities
Organize training data
Generate dataset structure
Prepare files for YOLO training
Assist in dataset management
make_all_txt_empty.py

Annotation utility script.

#### Responsibilities
- Clear label files
- Reset annotation contents
- Prepare dataset for relabeling
Useful when rebuilding datasets from scratch.

#### sort.py

SORT (Simple Online and Realtime Tracking) implementation.

##### Responsibilities
- Track detected riders between frames
- Maintain object identities
- Reduce duplicate detections
- Improve temporal consistency
##### Benefits
- Stable tracking IDs
- Better video analytics
- Reduced false detections

#### data.yaml

YOLO dataset configuration file.

Contains:
```
train:
val:
test:

nc:
names:
```
Used during YOLOv8 training.

#### Weights/helmet.pt

Trained YOLO model weights.

Purpose

Stores the learned parameters of the helmet detection model.

Used for:

- Image inference
- Video inference
- Real-time deployment

#### Weights/helmet.pt
Trained YOLO model weights.

#### Purpose
Stores the learned parameters of the helmet detection model.

Used for:

- Image inference
- Video inference
- Real-time deployment

#### Dataset

The project uses a custom helmet detection dataset exported in YOLOv8 format.

Dataset structure:
```
train/
valid/
test/
```
Each split contains:
```
images/
labels/
```
Annotations are stored in YOLO format.

### Detection Pipeline
```
Input Image / Video
          │
          ▼
Frame Extraction
          │
          ▼
YOLOv8 Inference
          │
          ▼
Helmet Classification
          │
          ▼
Bounding Box Generation
          │
          ▼
Visualization
          │
          ▼
Output Display

```

### Installation
Clone Repository
```
git clone https://github.com/Oudarja/Bike_Helmet_Detector.git
cd Bike_helmet_detector
```
Create Virtual Environment
```
python -m venv .helmet
source .helmet/bin/activate
```
Install Dependencies
```
pip install -r req.txt
```

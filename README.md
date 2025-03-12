# YOLO-Based Real-Time Object Detection

![YOLO Object Detection](https://upload.wikimedia.org/wikipedia/commons/8/8c/YOLO_object_detection.gif)

## 📌 Overview
This project implements **real-time object detection** using the **YOLO (You Only Look Once)** model and OpenCV. The script captures video from a webcam, detects specified objects, and triggers an alert when a match is found. Detected frames are saved automatically for future reference.

## 🚀 Features
- Uses **YOLO** for accurate and fast object detection
- Real-time processing with a webcam
- Configurable **object detection queries**
- Saves detected frames with timestamps
- Prints alerts when specified objects are detected

## 🛠️ Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/yolo-object-detection.git
   cd yolo-object-detection
   ```
2. Install dependencies:
   ```bash
   pip install ultralytics opencv-python
   ```
3. Download the YOLO model weights:
   ```bash
   wget https://github.com/ultralytics/assets/releases/download/v8/yolov8n.pt
   ```

## 🏃‍♂️ Usage
Run the script to start real-time detection:
```bash
python detect.py
```

### 📷 Example Output:
```
2024-03-12 14:35:21:  person detected
Saved: data/processed_03_12_2024_14_35_21.jpg
```

## 📝 Configuration
Modify the following parameters inside `detect.py`:
- **Model Selection:** Change `yolo8n.pt` to a different YOLO model for better accuracy.
- **Object Queries:** Update `obj_queries` to specify the objects you want to detect.
- **Frame Save Directory:** Ensure the `data/` directory exists before running.

## 📌 Future Enhancements
- Add support for multiple cameras
- Implement email or push notifications
- Improve performance with threading

## 📜 License
This project is licensed under the MIT License. Feel free to use and modify it!

### 🔗 Connect with Me
[GitHub](https://github.com/keyvanaghaei) | [LinkedIn](https://www.linkedin.com/in/keyvan-aghaei/) 


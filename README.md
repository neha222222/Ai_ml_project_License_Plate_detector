# Ai_ml_project_License_Plate_detector

This program utilizes the Ultralytics YOLO (You Only Look Once) model to detect number plates in images or real-time video streams. The YOLO model has been trained on a dataset and is capable of accurately identifying and localizing number plates.

# Requirements:
- Python 3.x
- ultralytics package
- OpenCV (cv2) package

# Installation:
1. Install Python 3.x from https://www.python.org/downloads/ if not already installed.
2. Install the required packages by running the following commands:
   - pip install ultralytics
   - pip install opencv-python

# Usage:
1. Ensure that the trained YOLO model file (e.g., 'best.pt') is present in the same directory as the script.
2. Run the script using the Python interpreter: python <script_name.py>

# Functionality:
1. The program opens the default camera (Webcam) to capture real-time video frames by setting the 'source' parameter to 0.
2. The YOLO model is used to predict number plate detections on each frame.
3. The predicted results are displayed on the screen and stored in the 'results' variable.
4. If a number plate is detected (results.pred[0] is not None), the corresponding image frame is saved as 'result.jpg'.
5. The program continues to capture frames and detect number plates until the 'q' key is pressed or 5 seconds have elapsed.
   - Note: Currently, the 'q' key functionality is commented out in the code.

Important Notes:
- The YOLO model file 'best.pt' should be a trained model specifically for number plate detection. Replace it with the appropriate model if needed.
- You can modify the source parameter to use a different video source (e.g., file path or camera index) if desired.
- Make sure the necessary dependencies are installed and accessible before running the script.

Credits:
- Ultralytics YOLO: https://github.com/ultralytics/yolov5
- OpenCV: https://opencv.org/

from ultralytics import YOLO
from ultralytics.yolo.v8.detect.predict import DetectionPredictor
import time
import cv2

# model = YOLO("yolov8n.pt")
model=YOLO("best.pt")
start_time = time.time()
# i want to use a key q to quit the program
while True:
    results = model.predict(source=0, show=True)
    print(results)
    # save the result to a file if a number plate is detected
    if results.pred[0] is not None:
        cv2.imwrite("result.jpg", results.imgs[0])
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    if time.time() - start_time > 5:
        break

cv2.destroyAllWindows()
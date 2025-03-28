from ultralytics import YOLO
import cv2 as cv2
import time
import datetime

def alarm(ob):
    print(str(datetime.datetime.now())+':  '+str(ob))

# Load the YOLO11 model
model = YOLO("yolo11n.pt")
# initialize the camera
cam = cv2.VideoCapture(0)
obj_queries=['person']
flag=0

while True:
    s, img = cam.read()
    flag=0
    if s:    
        # Run inference on an image
        results = model(img, verbose=False)
        detected_names=set([model.names[int(x)] for x in results[0].boxes.cls])
        for ob in detected_names:
            if ob in obj_queries:
                
                alarm(ob)
                # Display results
                results[0].save('data/processed_'+str(datetime.datetime.now().strftime("%m_%d_%Y_%H_%M_%S"))+'.jpg')
                flag=1
                break
        if(len(detected_names)==0 or flag==0):
            print(str(datetime.datetime.now())+':  '+'----------------')
        time.sleep(0.5)
    else:
        time.sleep(0.5)

from ultralytics import YOLO
import cv2
import cvzone
import math

i=cv2.VideoCapture(0)
i.set(3,1280)
i.set(4,720)
model=YOLO("yolo weights/yolov8x.pt")

classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
             "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
             "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
             "handbag","tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
             "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup", "fork", "knife",
             "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli", "carrot", "hot dog", "pizza",
             "donut", "cake", "chair", "sofa", "pottedplant", "bed", "diningtable", "toilet", "tvmonitor", "laptop",
             "mouse", "remote", "keyboard", "cell phone", "microwave", "oven", "toaster", "sink", "refrigerator", "book",
             "clock", "vase", "scissors", "teddy bear", "hair drier", "toothbrush"] 

while True:
    success, img =i.read()
    results=model(img, stream=True)
    for r in results:
        boxes=r.boxes
        for box in boxes:

            #for bounding box
            x1,y1,x2,y2=box.xyxy[0]
            x1,y1,x2,y2=int(x1), int(y1), int(x2), int(y2)
            print(x1,y1,x2,y2)
            cv2.rectangle(img, (x1,y1),(x2,y2),(255,0,255),3)
            w,h=x2-x1,y2-y1
            cvzone.cornerRect(img,(x1,y1,w,h))
            
            #for confidence
            conf=math.ceil((box.conf[0]*100))/100
            print(conf)
            

            #class name
            cls=int(box.cls[0])
            cvzone.putTextRect(img,f'{classNames[cls]} {conf}',(max(0,x1), max(35,y1)))
            print()




    cv2.imshow("Image", img)
    cv2.waitKey(1)

./darknet detector demo cfg/coco.data cfg/yolov4-tiny.cfg yolov4-tiny.weights 'nvarguscamerasrc ! video/x-raw(memory:NVMM), width=(int)1024, height=(int)720,format=(string)NV12, framerate=(fraction)30/1 ! nvvidconv flip-method=0 ! video/x-raw, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink'


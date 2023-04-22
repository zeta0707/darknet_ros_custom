# overwrite custom train wieghts and cfg
darknet_ros modification for Jetson and custom dataset

ROS code: ZETA7, zeta0707@gmail.com  
Colab notebook: ZETA7, zeta0707@gmail.com  
https://colab.research.google.com/drive/1B6JZp6YvDtxhZKTIN7e3qpQFPcEPM1YK#scrollTo=NjKzw2TvZrOQ

```
├── CMakeLists.txt
├── config
│   ├── ros_csi.yaml
│   ├── ros_webcam.yaml
│   ├── ros.yaml
│   ├── yolov4_jessiarm.yaml
│   ├── yolov4_jessicar.yaml
│   └── yolov4.yaml
├── Images
├── launch
│   ├── yolo_v4_jessiarm.launch
│   └── yolo_v4_jessicar.launch
├── README.md
└── yolo_network_config
    ├── cfg
    │   ├── yolov4-tiny.cfg
    │   ├── yolov4-tiny-gostop.cfg
    │   └── yolov4-tiny-jessiarm.cfg
    └── weights
        ├── yolov4-tiny-gostop.weights
        ├── yolov4-tiny-jessiarm.weights
        └── yolov4-tiny.weights
```

## Yolov4 tiny 
```
yolov4.yaml   
yolov4-tiny.cfg   
yolov4-tiny.weights: https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v4_pre/yolov4-tiny.weights   
```

## Jessicar traffic signal
```
yolov4_jessicar.yaml      
yolov4-tiny-gostop.cfg      
yolov4-tiny-gostop.weights   
``` 
<p align="center">
    <img src="/Images/jessicar1.png" width="400" />
</p>

## Jessiarm custom training
```
yolov4_jessiarm.yaml
yolov4-tiny-jessiarm.cfg   
yolov4-tiny-jessiarm.weights 
```  
<p align="center">
    <img src="/Images/jessiarm2_1.png" width="400" />
</p>


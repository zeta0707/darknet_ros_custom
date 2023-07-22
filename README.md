# overwrite custom train wieghts and cfg
darknet_ros modification for Jetson and custom dataset

ROS code: ZETA7, zeta0707@gmail.com  
Colab notebook: ZETA7, zeta0707@gmail.com  
https://colab.research.google.com/drive/1B6JZp6YvDtxhZKTIN7e3qpQFPcEPM1YK#scrollTo=NjKzw2TvZrOQ

```
├── CMakeLists.txt
├── config
│   ├── ros.yaml
│   ├── yolov4_jessiarm.yaml
│   ├── yolov4_jessicar.yaml
│   └── yolov4.yaml
├── Images
├── launch
│   ├── yolov4_jessiarm.launch
│   └── yolov4_jessicar.launch
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

## Yolov4-tiny - Object tracking
Pretranined model
```
yolov4.yaml   
yolov4-tiny.cfg   
yolov4-tiny.weights: https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v4_pre/yolov4-tiny.weights   
```

## Jessicar custom training - Reacting to traffic light
```
yolov4_jessicar.yaml      
yolov4-tiny-gostop.cfg      
yolov4-tiny-gostop.weights   
``` 
<p align="center">
    <img src="/Images/go.png" width="400" />
    <img src="/Images/left.png" width="400" />
    <img src="/Images/stop.png" width="400" />
    <img src="/Images/right.png" width="400" />
</p>

I used below picture for training.
<p align="center">
    <img src="/Images/trafficSign.jpg" width="600" />
</p>

## Jessiarm custom training - Pick and Place two objects
```
yolov4_jessiarm.yaml
yolov4-tiny-jessiarm.cfg   
yolov4-tiny-jessiarm.weights 
```  
<p align="center">
    <img src="/Images/jessiarm.png" width="400" />
</p>


from ultralytics import YOLO

model=YOLO('best.pt')

model.predict(source=0,save=True,conf=0.4,show=True)


#coding:utf-8
from ultralytics import YOLO

# 加载模型
model = YOLO("yolov8n.pt")  # 加载预训练模型
# Use the model
if __name__ == '__main__':
    # Use the model
    results = model.train(data='datasets/helmetData/data.yaml', epochs=150, batch=32,imgsz=640,device=0,cache=True,workers=32)  # 训练模型
    # 将模型转为onnx格式
    # success = model.export(format='onnx')




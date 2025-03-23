import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO


train_dir = "./content/datasets/license-plate-dataset/archive/images/train"
val_dir = "./content/datasets/license-plate-dataset/archive/images/val"


classes = ["license_plate"]

# Create YAML content
data_yaml_content = f"""
train: {train_dir}
val: {val_dir}

nc: {len(classes)}  # Number of classes
names: {classes}  # Class names
"""

# Save to a file
yaml_path = "data.yaml"
with open(yaml_path, "w") as f:
    f.write(data_yaml_content)
    
    
model = YOLO('yolov8n.pt')


results = model.train(
    data="./data.yaml",
    epochs=1,
    imgsz=640,
    lr0=0.0005,
    batch=32,
    lrf=0.1,
    augment=True,
    device="mps"
)

model.save('trained_model.pt')
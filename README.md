# This is for learning purpose only
![detected](https://github.com/user-attachments/assets/cfaef7b4-ee18-4985-bbb5-893fa8811289)

this use real car park in front of my home
[Data is from kaggle](https://www.kaggle.com/code/keo123/license-plate-detection-with-yolov8/edit)

# Usage 

### Set up env
```bash
# Install the required environment
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

### Train your modal

```
sh dl_data.sh
python3 train.py
```

### Update your modal path and test
```
python3 detect.py
```

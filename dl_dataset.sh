
mkdir -p ./datasets/content
curl -L -o ./datasets/content/license-plate-dataset.zip https://www.kaggle.com/api/v1/datasets/download/ronakgohil/license-plate-dataset

unzip ./datasets/content/license-plate-dataset.zip -d ./datasets/content/license-plate-dataset

mkdir ./datasets/content/datasets
mv ./datasets/content/license-plate-dataset ./datasets/content/datasets/
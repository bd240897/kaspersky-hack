# torch
import torch
import torch.nn as nn
import torch.optim as optim
from torch.optim import lr_scheduler
import torchvision
from torchvision import datasets, models, transforms

# python
import os
import json
from pathlib import Path
from os.path import basename
import requests
from io import BytesIO

# ml-modules
import numpy as np

# img
from PIL import Image

# django
from django.conf import settings

# turn off warnings
import warnings
warnings.filterwarnings('ignore')

# КОНСТАНТЫ
if __name__ == '__main__':
    BASE_DIR_TEMP = r"C:\Games\Python_works\kaspersky-hack\api"
else:
    BASE_DIR_TEMP = settings.BASE_DIR

APP_NAME = 'predictor'
FOLDER_NAME = 'ml_models'
PATH_MODEL_WEIGHTS = os.path.join(BASE_DIR_TEMP, APP_NAME, FOLDER_NAME, "parasites_alexnet", 'alexnet_waights.pth')
IMG_URL = "https://p.calameoassets.com/160810152536-3dbd84e9398a3a4ccc1ad50cb4651692/p1.jpg"

class BaseLine():
    """Фильтр. Получает ссылку на фото jpg и дает предсказание 1го из 2х классов"""

    def __init__(self):
        self.get_map_labels()
        self.get_transformer()
        self.create_model()
        self.load_model_weights()

    def get_map_labels(self):
        # декодированием меток
        self.map_labels = ['true', 'false']

    def get_transformer(self):
        # трансформация входных данных
        self.data_transforms = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(244),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ])

    def create_model(self):
        # создание модели
        model_extractor = models.alexnet(weights=False)
        model_extractor.classifier = nn.Linear(9216, 2)
        self.model = model_extractor

    def load_model_weights(self):
        # загрузка весов модели
        self.model.load_state_dict(torch.load(PATH_MODEL_WEIGHTS))

    def _check_img_extension(self, url):
        """Проверка расширения по урлу"""

        img_extension = url.rsplit('/', 1)[1].rsplit('.', 1)[1]
        if not img_extension in ['jpg', 'JPG']:
            raise Exception("Расширение файла не .jpg")

    def _check_img_verify(self, img):
        """Проверка картинки с помощью Pillow"""

        try:
            im = Image.open(img)
            im.verify()  # I perform also verify, don't know if he sees other types o defects
            im.close()  # reload is necessary in my case
        except:
            raise Exception("Ошибка чтения файла")

    def _load_file(self, url=IMG_URL):
        # проверка расширения файла
        self._check_img_extension(url)

        # загрузка изображения из инета
        response = requests.get(url)
        content = BytesIO(response.content)

        # проверка что это картинка
        self._check_img_verify(content)

        # Открытие изображения и его траснформация
        loaded_img = Image.open(content)
        transformed_img = self.data_transforms(loaded_img)
        return transformed_img

    def predict_file(self, url=IMG_URL):
        img = self._load_file(url)

        # делаем предсказание
        with torch.no_grad():
            self.model.eval()
            logit = self.model(img.unsqueeze(0))
            probs = torch.nn.functional.softmax(logit, dim=-1).numpy()
            # print(probs)
            id = np.argmax(probs)
            # print(id)
            predicted_class = self.map_labels[id]
            # print(predicted_class)
        return predicted_class



if __name__ == '__main__':
    IMG_URL = "https://p.calameoassets.com/160810152536-3dbd84e9398a3a4ccc1ad50cb4651692/p1.jpg"
    try:
        model = BaseLine()
        prediction = model.predict_file(url=IMG_URL)
        print(prediction)
    except Exception as e:
        print(e)




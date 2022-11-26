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
import matplotlib.pyplot as plt

# django
from django.conf import settings

if __name__ == '__main__':
    BASE_DIR_TEMP = r"C:\Users\Дмитрий\WebstormProjects\LearnVue\api"
else:
    BASE_DIR_TEMP = settings.BASE_DIR

APP_NAME_TEMP = 'core'
PATH_MODEL_WEIGHTS = os.path.join(BASE_DIR_TEMP, APP_NAME_TEMP, "ml_alexnet", 'alexnet_waights.pth')
IMG_URL = "https://p.calameoassets.com/160810152536-3dbd84e9398a3a4ccc1ad50cb4651692/p1.jpg"

# декодированием меток
map_labels = ['other', 'poop']

# трансформация входных данных
data_transforms = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(244),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

# создание модели
model_extractor = models.alexnet(pretrained=False)
model_extractor.classifier = nn.Linear(9216, 2)

# загрузка весов модели
model_extractor.load_state_dict(torch.load('alexnet_waights.pth'))

# загрузка изображения из инета и его трансформация
response = requests.get(IMG_URL)
img_loaded = Image.open(BytesIO(response.content))
transformed_img = data_transforms(img_loaded)

# делаем предсказание
with torch.no_grad():
    model_extractor.eval()
    logit = model_extractor(transformed_img.unsqueeze(0))
    probs = torch.nn.functional.softmax(logit, dim=-1).numpy()
    print(probs)
    id = np.argmax(probs)
    print(id)
    predicted_class = map_labels[id]
    print(predicted_class)

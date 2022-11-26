# Принцип отправки изображения

## Логика использования БД

![](<../.gitbook/assets/Диаграмма без названия.drawio (1).png>)

1. В таблице Diseases есть диагнозы и их описание

```
{
    "id": 1,
    "name": "Кровь"
    "discription": "Кровь в фекалиях"
}
```

2\. Пользователь отравляет фото через сайт

3\. В базе данных создается экземпляр в таблички "RequestPhoto" c пустыми полями "photo" и "diseases"

```
{
    "id": 1,
    "pet": "Пушок",
    "photo": None
    "date_creation": 10,
    "diseases": {}
}
```

4\. Фото сохраняется в БД в поле "photo"&#x20;

```
{
    "id": 1,
    "pet": "Пушок",
    "photo": "https://pixelbox.ru/wp-content/uploads/2021/02/mult-ava-instagram-69.jpg"
    "date_creation": 10,
    "diseases": {}
}
```

5\. url фото из таблица "PredictionPhoto" отправляется на cnn-filter (микросервис)

```
- если это фекаллии то ответ
{
    type: poops
}
- если не фекалии отдаем ответ
{
    type: other
}
```

6\. url фото из таблица "PredictionPhoto" отправляется на cnn-prediction (микросервис)&#x20;

```
{
    parasites: True
    blood: False
}
```

7\. В таблицу "RequestPhoto" в поле "diseases" записываются эти дагнозы в поле "diseases"

```
{
    "id": 1,
    "pet": "Пушок",
    "photo": "https://pixelbox.ru/wp-content/uploads/2021/02/mult-ava-instagram-69.jpg"
    "date_creation": 10,
    "diseases": {1,2}
}
```

# Scanner port
В данном проекте был реализован 1 из REST API запросов GET. Данный GET запрос возвращает порт и его статус (открытый или закрытый).
Основной маршрут:

/scan<ip>/<begin_port>/<end_port> 
## Запуск
Запустить сервер можно с помощью команды

```python3 -m venv venv```

```source venv/bin/activate```

```pip install -r requirements.txt```

```python3 main.py```


Данный проект выполнен как тестовое задание.

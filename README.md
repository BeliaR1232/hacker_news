# Проект Hacker_News

Приложение для парсинга сайта Hacker News - https://news.ycombinator.com, сохранения новостей в базу данных и возврат информации по GET запросу с возможностью сортировки и указания лимита новостей. 

# Запуск

Для работы проекта понадобится Python3.8 или выше MySQL, Redis-server.
+ устанавливаем зависимости:
    + pip install -r requirements.txt  
    
+ нужно настроить параметры подключения к MySQL в settings:
  + указать имя бд, юзера, пароль для юзера

      
+ создать файлы миграции и запустить миграцию:
    + python manage.py makemigrations  
    + python manage.py migrate  
      
+ запустить сбор новостей:
  + python3 manage.py pars_news  
    
+ запустить сервер
  + python manage.py runserver  
    
+ так же можно запустить автоматический сбор данных. 
  По умолчания парсинг страницы и сохранение будет происходить каждый час (можно настроить в коде команды)
  + запустить воркер(Redis должен быть запущен) и планировщик:
    + python3 manage.py rqworker
    + python3 manage.py scheduler_news
    
# Инструкция 

Для получения списка существующих объектов используется HTTP метод GET.
+ адрес http://127.0.0.1:8000/posts/
  
  
# Сортировка
Для новостей реализованна функция сортировки по всем полям. По умолчанию сортировка производиться по ID:
+ для сортировки нужно добавить параметр ***ordering=title/-title, id/-id, url/-url*** (по возрастанию и убыванию соответственно)
 
Есть возможность запросить подмножество данных, указав offset и limit. По умолчанию API возвращает 5
постов.
+ для запроса нужно добавить параметры ***limit и/или offset***   
  
Если указан некорректный параметр, сортировка и запрос подмножества происходит по дефолтным значениям.

  
# Примеры  
  
Получение списка новостей:
+ curl -X GET 'http://127.0.0.1:8000/posts/'
    + ответ: [{"id":1,"title":"Github1s – One second to read GitHub code with VS Code","url":"https://github.com/conwnet/github1s","date_created":"2021-02-10T09:28:10.243727Z"},{"id":2,"title":"Infinitely zooming botanical floral paradise painting","url":"http://arkadia.xyz/","date_created":"2021-02-10T09:28:10.264116Z"}...}]
      
Сортировка новостей:
+ curl -X GET 'http://127.0.0.1:8000/rooms/?ordering=title,date_created'
    + ответ: [{"id":1,"title":"Github1s – One second to read GitHub code with VS Code","url":"https://github.com/conwnet/github1s","date_created":"2021-02-10T09:28:10.243727Z"},{"id":2,"title":"Infinitely zooming botanical floral paradise painting","url":"http://arkadia.xyz/","date_created":"2021-02-10T09:28:10.264116Z"}...}]  
      
Получение подмножество данных:
+ curl -X GET 'http://127.0.0.1:8000/bookings/?limit=10&offset=10'
    + ответ: [{"id":11,"title":"Github1s – One second to read GitHub code with VS Code","url":"https://github.com/conwnet/github1s","date_created":"2021-02-10T09:28:10.243727Z"},...}]  
    
# Инструменты
+ [Redis](https://redis.io/)
+ [MySQL](https://www.mysql.com/)
+ [Python](https://www.python.org/)
+ [Django](https://www.djangoproject.com/)
+ [Django REST framework](https://www.django-rest-framework.org/)
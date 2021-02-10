import requests
from bs4 import BeautifulSoup


URL = 'https://news.ycombinator.com/'


def get_html(url):
    # GET запрос по урлу, получения html кода страницы
    try:
        req = requests.get(url=url)
    except requests.exceptions.ConnectionError:
        print('Ошибка соединения. Проверьте подключение к интернету.')
    else:
        return req.text


def parser(html):
    # Парсинг нужной информации
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.find_all('a', class_='storylink')
        return items


def get_data(items):
    # Структурирование данных
    data = list()
    if items:
        for item in items:
            data.append({'title': item.get_text(strip=True),
                         'url': item.get('href')})
        return data


def save_data_in_db(model):
    # Запись данных в базу, если новость уже есть в бд, она не будет дублироваться
    html = get_html(URL)
    items = parser(html)
    data = get_data(items)

    if data:
        for item in data:
            if not model.objects.filter(title=item['title']).exists():
                entity = model(title=item['title'], url=item['url'])
                entity.save()
            else:
                continue
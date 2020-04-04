from datetime import datetime, date, time
import urllib.request
from bs4 import BeautifulSoup
import week


# функция для получения url сайта
def Site(url):
    """
    input : url code
    output : bytes
    """
    response = urllib.request.urlopen(url)
    return response.read()


# сам парсер
def Parse(html):
    """
    input : html code
    output : str
    """
    soup = BeautifulSoup(html)
    code = soup.get_text()
    dick = code.split('Преподаватель/аудитория')[1]  # ищем нужный тег
    result = dick[:1126]  # удаляем ненужный конец
    day = week.Week(result)
    if day == 'Сейчас нижняя неделя' or day == "Cледующая неделя нижняя нижняя неделя" :
        result = dick[:1005]
    result = result.replace('10-1511-50', '10-15 11-50').replace('12-0013-35', '12-00 13-35').replace('14-1515-50', '14-15 15-50').replace('8-3010-05', '8-30 10-05')
    return result



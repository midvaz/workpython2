from vk_api import longpoll
from vk_api.longpoll import VkEventType, VkLongPoll
import students
import vk_api
import message
import random


def random_id():
    Random = 0
    Random += random.randint(0, 1000000000000)
    return Random

#Хуй
def glossing(vk_session, fuck): # Эту функцию вызываем из файла "message"
    longpoll = VkLongPoll(vk_session)
    vk = vk_session.get_api()

    while True:
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                if event.text.lower() == 'назад': # Если пользователь вводит это значение, то
                    vk.messages.send(             # Его выкидывают в начальные кнопки
                        user_id=event.user_id,    # Для выбора другой операци
                        message="Зачем было заходить?",
                        keyboard=open("keyboard.json", "r", encoding="UTF-8").read(),
                        random_id=random_id()
                    )
                else:
                    # Получаем от пользователя номер студента и его оценку
                    number = event.text.lower() # Номер студента
                    for events in longpoll.listen():
                        if events.type == VkEventType.MESSAGE_NEW and event.to_me:
                            gloss = events.text.lower() # Оценка для студента
                            return students.student_info(number, gloss) # Возвращаем значение из функции
                                                                        # student_info из файла students

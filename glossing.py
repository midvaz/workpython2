from vk_api import longpoll
from vk_api.longpoll import VkEventType, VkLongPoll
import students


def glossing(vk_session):
    longpoll = VkLongPoll(vk_session)
    vk = vk_session.get_api()

    while True:
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                number = event.text.lower()
                for events in longpoll.listen():
                    if events.type == VkEventType.MESSAGE_NEW and event.to_me:
                        gloss = events.text.lower()
                        return students.student_info(number, gloss)
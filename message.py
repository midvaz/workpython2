import random
from vk_api.longpoll import VkLongPoll, VkEventType
import week
import pars
import vk_api
import glossing


def random_id():
    Random = 0
    Random += random.randint(0, 1000000000000)
    return Random


fuck = pars.Parse(pars.Site('https://edu.donstu.ru/Rasp/Rasp.aspx?group=32353&sem=2'))

vk_session = vk_api.VkApi(token="4e3f2af11078b879a7a574564ca5d14f3eb100cdb69c6ff953e1096c5a67f5a6d06233a295e52bc416026")


# Функция, чтобы можно было отправлять сообщение одно и тому же
def Mess(fuck, vk_session):
    longpoll = VkLongPoll(vk_session)
    vk = vk_session.get_api()

    event = open("C:\\Users\\mi28d\\Desktop\\vkbot\\events.txt", encoding='utf8')
    lines = ""

    for line in event:
        lines += line

    students_numbers = open("C:\\Users\\mi28d\\Desktop\\vkbot\\students_numbers", encoding='utf8')
    linet = ''

    for line in students_numbers:
        linet += line
    
    her_otvet1 = ['Для кого, блять, кнопки сделали?', 'Тыкай по кнопочкам', 'ъУъ сука', 'КНОПКИ !!!',
                  'Сейчас разозлюсь']
    her_otvet2 = ['Не ебу, хули тебе надо....', 'Че?', 'А?', 'Выплюнь хуй и напиши нормально',
                  'Не зря ваша группа самая тупая']
    i = 0
    k = 1
    while True:
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
# пусть пока будет так но потом нужно будет это норм сделать
# может быть стоит это потом вынести в отдельную фу-цию
                if event.user_id == 263542561 : 
                    print("прислал","Александр самый лучший воще","написал",event.text)
                if event.user_id == 293470132 : 
                    print("прислал","Олежа","написал",event.text)
                else :
                    print("прислал","Ноунейм с айди",event.user_id,"написал",event.text)

                if event.text.lower() == 'расписание':  # Нижний регистр.
                    vk.messages.send(
                        user_id=event.user_id,
                        message=fuck,
                        keyboard=open("C:\\Users\\mi28d\\Desktop\\vkbot\\keyboard.json", "r", encoding="UTF-8").read(),
                        random_id=random_id()
                    )
                    k = 2
                elif event.text.lower() == 'неделя':
                    vk.messages.send(
                        user_id=event.user_id,
                        message=week.Week(fuck),
                        keyboard=open("C:\\Users\\mi28d\\Desktop\\vkbot\\keyboard.json", "r", encoding="UTF-8").read(),
                        random_id=random_id()
                    )
                    k = 2
                elif event.text.lower() == 'другие команды':
                    vk.messages.send(
                        user_id=event.user_id,
                        message='Ты взломать мою жепку',
                        keyboard=open("C:\\Users\\mi28d\\Desktop\\vkbot\\keyboard.json", "r", encoding="UTF-8").read(),
                        random_id=random_id()
                    )
                    k = 2

                elif event.text.lower() == "события":
                    vk.messages.send(
                        user_id=event.user_id,
                        message=lines,
                        keyboard=open("C:\\Users\\mi28d\\Desktop\\vkbot\\keyboard.json", "r", encoding="UTF-8").read(),
                        random_id=random_id()
                    )
                    k = 2

                elif event.text.lower() == 'голосование':

                    vk.messages.send(
                        user_id=event.user_id,
                        message=linet, # Вывод сообщения о входе в режим голосования.
                        keyboard=open("C:\\Users\\mi28d\\Desktop\\vkbot\\glossing_keyboard.json", "r", encoding="UTF-8").read(), # Вызываем главиатуру голосования.
                        random_id=random_id()
                    )
                    vk.messages.send(
                        user_id=event.user_id,
                        message=glossing.glossing(vk_session, fuck), # Вызываем метод "голосование"
                        keyboard=open("C:\\Users\\mi28d\\Desktop\\vkbot\\keyboard.json", "r", encoding="UTF-8").read(),
                        random_id=random_id()
                    )
                    k = 3
# нужно что нибудь норм сделать с фразами потому что сейчас это ужастный костыль
# может быть стоит это потом вынести в отдельную фу-цию
                else:
                    if k != 3 :
                        if i < 4:
                            vk.messages.send(
                                user_id=event.user_id,
                                message=random.choice(her_otvet1),
                                keyboard=open("C:\\Users\\mi28d\\Desktop\\vkbot\\keyboard.json", "r", encoding="UTF-8").read(),
                                random_id=random_id()
                            )
                            i += 1
                        else:
                            vk.messages.send(
                                user_id=event.user_id,
                                message=random.choice(her_otvet2),
                                keyboard=open("C:\\Users\\mi28d\\Desktop\\vkbot\\keyboard.json", "r", encoding="UTF-8").read(),
                                random_id=random_id()
                            )

# Создаем список студентов и их рейтинга
students = dict()

students['1'] = ['Олег', 0]
students['2'] = ['Александр', 0]
students['3'] = ['Максим', 0]
students['4'] = ['Игорь', 0]
students['5'] = ['Чувак', 0]


def student_id(number, user_id):
    i = 0
    lines = ""
    while i < len(students):
        if number in students:

            file_name = students[number]
            event = open(file_name[0] + ".txt", encoding='utf8',)

            for line in event:
                lines += line

            if str(user_id) in lines:
                return False
            else:
                events = open(file_name[0] + ".txt", 'w')
                events.write(str(user_id) + '\n')
                event.close()
                return True


# отвечает на ввод числа (норм это число или не проходит по критериям)
def student_info(number, gloss, user_id):
    i = 1
    while i < 25:
        if (number in students) and ((float(gloss) >= 1) and (float(gloss) <= 5)):  # Проверка на вход в диапазон оценок
            if student_id(number, user_id):
                rating = students[number]
                rating[1] += float(gloss)
                return students[number]
                i += 1
            else:
                return "Ты борзый самый?"
        else:
            return "Неправильное число"


# Пока не работает
# Была битва бомжей

def ratingg(number):
    i = 0

    while i <= len(students):
        i += 1
        if number in students:
            rating_student = students[number]
            sredniy_rating = rating_student[1] / 10
            return sredniy_rating
        else:
            return "Error"

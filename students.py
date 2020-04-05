# Создаем список студентов и их рейтинга
students = dict()

students['1'] = ['Олег', 0]
students['2'] = ['Александр', 0]
students['3'] = ['Максим', 0]
students['4'] = ['Игорь', 0]
students['5'] = ['Чувак', 0]


# отвечает на ввод числа (норм это число или не проходит по критериям)
def student_info(number, gloss):
    i = 1
    while i < 25:
        if (number in students) and ((float(gloss) >= 1) and (float(gloss) <= 5)):  # Проверка на вход в диапазон оценок
            rating = students[number]
            rating[1] += float(gloss)
            return students[number]
            i += 1
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

# Создаем список студентов и их рейтинга

# students = dict()
# rating = dict()

# students['1'] = 'Олег'
# students['2'] = 'Александр'
# students['3'] = 'Максим'
# students['4'] = 'Игорь'
# students['5'] = 'Чувак'

rating['1'] = 0
rating['2'] = 0
rating['3'] = 0
rating['4'] = 0
rating['5'] = 0

# можно внутри создать еще и масив добляя туда оценки и коментарии
students = {
    '1' : Олежа 
    '2' : Александр
    '3' : Максим
    '4' : Игорь
    '5' : Чувак
}

# отвечает на ввод числа (норм это число или не проходит по критериям)
def student_info(number, gloss):
    i = 1
    while i < 25:
        if (number in students) and ((float(gloss) >= 1) and (float(gloss) <= 5)): # Проверка на вход в диапазон оценок
            rating[number] += float(gloss)
            return students[number], " ", rating[number]
            i += 1
        else:
            return "Неправильное число"

# Пока не работает
# Была битва бомжей
def ratingg(number):
    i = 0
    
    while i <= len(rating) :
        i += 1
        if number in rating:
            sredniy_rating = rating[number] / 10
            return sredniy_rating
    else:
        return "Error"

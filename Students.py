import json
from datetime import datetime

# Функция для чтения студентов из файла
def read_students_from_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)  # Считываем JSON-данные
        for student in data:
            # Преобразуем строки даты в объекты datetime
            student['Дата_рождения'] = datetime.strptime(student['Дата_рождения'], '%Y-%m-%d')
            for exam in student['Зачётка']:
                exam['Дата_экзамена'] = datetime.strptime(exam['Дата_экзамена'], '%Y-%m-%d')
    return data

# Функция для ввода студентов через консоль
def add_students_from_console():
    students = []
    while True:
        full_name = input("Введите ФИО студента (или 'стоп' для завершения): ")
        if full_name.lower() == 'стоп':
            break

        # Получаем дату рождения
        birthdate_str = input("Введите дату рождения (год-месяц-день): ")
        birthdate = datetime.strptime(birthdate_str, '%Y-%m-%d')

        # Добавляем зачётку
        zachetka = []
        num_subjects = int(input("Введите количество предметов в зачётке (от 3 до 5): "))
        for _ in range(num_subjects):
            subject = input("Введите предмет: ")
            exam_date_str = input("Введите дату экзамена (год-месяц-день): ")
            exam_date = datetime.strptime(exam_date_str, '%Y-%m-%d')
            professor = input("Введите ФИО преподавателя: ")

            zachetka.append({
                'Предмет': subject,
                'Дата_экзамена': exam_date,
                'Преподаватель': professor
            })

        students.append({
            'ФИО': full_name,
            'Дата_рождения': birthdate,
            'Зачётка': zachetka
        })

    return students

# Основной код программы
choice = input("Вы хотите вводить студентов через консоль или считать из файла? (консоль/файл): ")

if choice.lower() == 'консоль':
    students = add_students_from_console()  # Ввод данных из консоли
elif choice.lower() == 'файл':
    filename = input("Введите имя файла (с расширением .json): ")
    students = read_students_from_file(filename)  # Считывание данных из файла
else:
    print("Неверный выбор")

if students:
    # Поиск самого младшего студента
    youngest_student = min(students, key=lambda s: s['Дата_рождения'])

    # Поиск самого старшего студента
    oldest_student = max(students, key=lambda s: s['Дата_рождения'])

    # Вывод ФИО и даты рождения самого младшего и самого старшего студентов
    print("Самый младший студент:", youngest_student['ФИО'], ", Дата рождения:", youngest_student['Дата_рождения'].strftime("%Y-%m-%d"))
    print("Самый старший студент:", oldest_student['ФИО'], ", Дата рождения:", oldest_student['Дата_рождения'].strftime("%Y-%m-%d"))
else:
    print("Нет данных о студентах")

import random
import string

def generate_password(length=12):
    # Убедимся, что длина пароля находится в пределах 8-32 символов
    if length < 8 or length > 32:
        raise ValueError("Длина пароля должна быть от 8 до 32 символов.")

    # Определим наборы символов, которые будут использоваться для генерации пароля
    letters = string.ascii_letters  # все буквы (заглавные и строчные)
    digits = string.digits          # все цифры
    special_chars = string.punctuation  # все специальные символы

    # Минимум по одному символу из каждой категории
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(special_chars)
    ]

    # Оставшиеся символы могут быть из любого из наборов
    for _ in range(length - len(password)):
        password.append(random.choice(letters + digits + special_chars))

    # Перемешиваем для большей случайности
    random.shuffle(password)

    # Преобразуем список в строку и возвращаем
    return "".join(password)

# Пример использования
generated_password = generate_password(12)  # 12-символьный пароль
print(generated_password)

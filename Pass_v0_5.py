import random
import string

# Функция для генерации пароля
def generate_password_v0_5(length=12):
    if length < 8 or length > 32:
        raise ValueError("Длина пароля должна быть от 8 до 32 символов.")

    # Основные наборы символов
    letters = string.ascii_letters  # Заглавные и строчные буквы
    digits = string.digits          # Цифры
    special_chars = string.punctuation  # Специальные символы

    
    # Просто заполним пароль случайными буквами
    password = [random.choice(letters) for _ in range(length)]

  
    # Возвращаем строку без перемешивания
    return "".join(password)

# Пример использования
generated_password = generate_password_v0_5(12) 
print(generated_password)

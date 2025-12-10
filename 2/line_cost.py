# Дана строка текста. Напишите программу для подсчета стоимости строки, исходя из того, что один любой символ
# (в том числе пробел) стоит 60 копеек. Ответ дайте в рублях и копейках в соответствии с примерами.
# Input 1:
# Привет, как дела?!
#
# Output 1:
# 10 р. 80 коп.
from decimal import Decimal


# text = str(input(""))
# sum = float(len(text) * 60 / 100)
# rub = int(sum)
# copeek = int((sum - rub) * 100)
# print(len(text) * 60 / 100)
# print(f'{rub} р. {copeek} коп.')

def calculate_string_cost(text):
    """
    Вычисляет стоимость строки: 60 копеек за символ.
    Возвращает строку с результатом в рублях и копейках.
    """
    # Количество символов в строке (включая пробелы и знаки препинания)
    char_count = len(text)

    # Стоимость в копейках: 60 копеек × количество символов
    total = char_count * 60

    # Переводим в рубли и копейки
    rubles = total // 100  # целые рубли
    kopecks = total % 100  # оставшиеся копейки
    print(f"{rubles} р. {kopecks} коп.")
    return f"{rubles} р. {kopecks} коп."


if __name__ == '__main__':
    assert calculate_string_cost("Привет, как дела?!") == "10 р. 80 коп."
    assert calculate_string_cost("Тимур - лучший математик на свете!!") == "21 р. 0 коп."
    assert calculate_string_cost(
        "Я собираюсь сделать ему предложение, от которого он не сможет отказаться.") == "43 р. 80 коп."
    assert calculate_string_cost("w") == "0 р. 60 коп."
    assert calculate_string_cost("Хьюстон, у нас проблема!") == "14 р. 40 коп."
    assert calculate_string_cost("«Обожаю запах напалма по утрам».") == "19 р. 20 коп."
    assert calculate_string_cost("«Элементарно, Ватсон».") == "13 р. 20 коп."
    assert calculate_string_cost("«Я тебе один умный вещь скажу, только ты не обижайся».") == "32 р. 40 коп."
    assert calculate_string_cost("BegekCyberSchool 3><3") == "12 р. 60 коп."

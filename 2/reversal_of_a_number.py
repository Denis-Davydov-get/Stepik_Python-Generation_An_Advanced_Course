# Дано пятизначное или шестизначное натуральное число.
# Напишите программу, которая изменит порядок его последних пяти цифр на обратный.
# Число нужно выводить без незначащих нулей

number = input("")
last_five = number[-5:]

# Переворачиваем их
reversed_five = last_five[::-1]

# Если число шестизначное, добавляем первую цифру в начало
if len(number) == 6:
    result_str = number[0] + reversed_five
else:  # пятизначное
    result_str = reversed_five

print(int(result_str))
# Дана строка, состоящая из слов, разделенных пробелами.
# Напишите программу, которая подсчитывает количество слов в этой строке.

def number_of_words(text: str) -> int:
    words = text.split()
    return len(words)


assert number_of_words("Hello world") == 2
assert number_of_words("Timur forever young") == 3
assert number_of_words("The future belongs to those who believe in beauty of their dreams") == 12
assert number_of_words("a b b cs bbb asdf") == 6
assert number_of_words("Beauty and wisdom are seldom found together") == 7
assert number_of_words("aa bb cc dd ee ffdd z") == 7
assert number_of_words("34v3 345t345t3 tr h re erthrt ttgg") == 7
assert number_of_words("slkrt e we hrthrtx sgsrtg") == 5
assert number_of_words("Тимур    Руслан    Роман  stepik") == 4


# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

from function import get_new_text

my_text = input('Введите текст: ')
print(f'Новый текст: {get_new_text(my_text)}')

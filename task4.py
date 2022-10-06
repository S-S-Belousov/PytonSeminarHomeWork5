# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

from function import encoding_file
from function import decoding_file

file_name=input('Введите имя файла для сжатия: ')
print(encoding_file(file_name))
file_name=input('Введите имя файла для восстановления: ')
print(decoding_file(file_name))



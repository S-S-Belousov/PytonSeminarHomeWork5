# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
from random import randint


candies = int(input('Введите общее количество конфет: '))
name1, name2 = input('Введите имя первого игрока: '), input(
    'Введите имя второго игрока. Для игры с ботом введите "Бот": ')
if randint(0, 2):
    user1_name, user2_name = name1, name2
else:
    user1_name, user2_name = name2, name1

user1_candies = 0
user2_candies = 0
max_candies = 28
print(f'Всего осталось: {candies} конфет')

while candies > 0:
    number_of_candies = 0
    if candies < 28:
        max_candies = candies
    if user1_name == 'Бот':
        if candies < 29:
            print(f'Бот забрал {candies} конфет')
            user1_candies += candies
            candies -= candies
        elif candies//28 == 1:
            print(f'Бот забрал {candies%28-1} конфет')
            user1_candies += candies % 28-1
            candies -= candies % 28-1
        else:
            print(f'Бот забрал {candies%28+1} конфет')
            user1_candies += candies % 28+1
            candies -= candies % 28+1
    else:
        while number_of_candies not in range(1, max_candies+1):
            number_of_candies = int(
                input(f'{user1_name}, введите количество конфет (от 1 до {max_candies}): '))
        candies -= number_of_candies
        user1_candies += number_of_candies
    if candies <= 0:
        print(f'Победил {user1_name}!')
        break
    print(f'Всего осталось: {candies} конфет')
    print(f'У пользователя {user1_name}: {user1_candies} конфет')
    number_of_candies = 0
    if candies < 28:
        max_candies = candies
    if user2_name == 'Бот':
        if candies < 29:
            print(f'Бот забрал {candies} конфет')
            user2_candies += candies
            candies -= candies
        elif candies//28 == 1:
            print(f'Бот забрал {candies%28-1} конфет')
            user2_candies += candies % 28-1
            candies -= candies % 28-1
        else:
            print(f'Бот забрал {candies % 28+1} конфет')
            user2_candies += candies % 28+1
            candies -= candies % 28+1
    else:
        while number_of_candies not in range(1, max_candies+1):
            number_of_candies = int(
                input(f'{user2_name}, введите количество конфет (от 1 до {max_candies}): '))
        candies -= number_of_candies
        user2_candies += number_of_candies
    if candies <= 0:
        print(f'Победил {user2_name}!')
        break
    print(f'Всего осталось: {candies} конфет')
    print(f'У пользователя {user2_name}: {user2_candies} конфет')

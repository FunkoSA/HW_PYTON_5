"""
Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета(или сколько вы зададите). Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
За один ход можно забрать не более чем 28 конфет(или сколько вы зададите). Тот, кто берет последнюю конфету - проиграл

"""
from random import randint


def clever_bot(number):
    '''Процедура хода умного бота, попробуй обыграй'''
    if not (number-1)%29:
        random_number = randint(1,28)
        print (f'осталось {number} конфет, бот забирает {random_number}')
        number = number - random_number
    elif number > 29:
        print (f'осталось {number} конфет, бот забирает {(number-1)%29}')
        number = number - (number-1)%29
    else:
        print (f'осталось {number} конфет, бот забирает {(number-1)} ')
        number = number - (number-1)
    return number

def simple_bot(number):
    '''Процедура хода обычного бота'''
    if number > 29:
       random_number = randint(1,28)
       print (f'осталось {number} конфет, бот забирает {random_number}')
       number = number - random_number
    else:
        random_number = randint(1,number)
        print (f'осталось {number} конфет, бот забирает {(random_number)} ')
        number = number - random_number
    return number

def take_candy (candy_amount):
    if candy_amount > 28:
        print (f'На столе лежит {candy_amount} кофет, можете забрать от 1 до 28 конфет')
        take_of_candy = input('Сколько конфет забираем: ')
        try:
             take_of_candy = int(take_of_candy)
             if 1 > take_of_candy or take_of_candy > 28:
                print(f'Введенное Вами количество конфет {take_of_candy} лежит вне лиапозона от 1 до 28')
                return take_candy (candy_amount)
        except:
            print(f'Введенное Вами {take_of_candy} не является числом!')
            return take_candy (candy_amount)
    else:
        print (f'На столе лежит {candy_amount} кофет, можете забрать от 1 до {candy_amount} конфет')
        take_of_candy = input('Сколько конфет забираем: ')
        try:
            int(take_of_candy)
            take_of_candy = int(take_of_candy)
            if 1 > take_of_candy or take_of_candy > candy_amount:
                print(f'Введенное Вами количество конфет {take_of_candy} лежит вне лиапозона от 1 до {candy_amount}')
                return take_candy (candy_amount)
        except:
            print(f'Введенное Вами {take_of_candy} не является числом!')
            return take_candy (candy_amount) 
    candy_amount = candy_amount - take_of_candy
    return candy_amount
def the_game(player1, player2,game_t):
    looser = ''
    n = 300
    round = 0
    if game_t == 1:
        f1 = take_candy
        f2 = take_candy
    elif game_t == 2:
        f1 = take_candy
        f2 = simple_bot
    else:
        f1 = take_candy
        f2 = clever_bot
    if randint(0,1) == 0:
        print (f'В результате жребия первым ходит {player1}')
        first_turn = player1
        second_turn = player2
    else:
        print (f'В результате жребия первым ходит {player2}')
        first_turn = player2
        second_turn = player1
        temp_f = f1
        f1 = f2
        f2 = temp_f


    while n > 0:
        round += 1
        print (f'{round} раудн')
        if not round%2:
            print (f'ходит {second_turn}:')
            n = f2(n)
        else:
            print (f'ходит {first_turn}:')
            n = f1(n)
    if not round%2:
        looser = second_turn
    else:
        looser = first_turn
    print (f'\nВ игре проиграл: {looser}\n')
    
    
while True:
    print('Для игры с двумя игроками выберите Р \n Для игры с простым ботом выберите Б \n Если хотите потягаться с умным ботом выберите  Х \n Для выхода выберите В')
    menu = input('>>> ').lower()
    if menu == 'в':
        break
    elif not (menu == 'р' or menu == 'б' or menu == 'х'):
        continue
    if menu == 'р':
        p1 = input('Ведиме имя первого игрока: ')
        p2 = input('Ведиме имя второго игрока: ')
        the_game(p1,p2,1)
    elif menu == 'б':
        p1 = input('Попробуй свои силы против машины, как тебя зовут: ')
        p2 = 'Бездушная машина'
        the_game(p1,p2,2)
    else:
        p1 = input('Суперкомпьютер принял вызов, как тебя зовут, Герой: ')
        p2 = 'Суперкомпьютер'
        the_game(p1,p2,3)


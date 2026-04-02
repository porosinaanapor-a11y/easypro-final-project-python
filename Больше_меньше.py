import random
print('Вы попали в игру Угадай число и у вас 5',' попыток ')
print('от 0 до 100')
n=random.randint(1,100)
pip=5
for i in range(pip+1):
    gg=int(input('Введите предполагаемое число:  '))
    if gg==n and pip!=0:
        print('Отлично! Вы угадали!')
        break
    elif gg!=n and pip==0:
        print('У вас закончились попытки')
        print('Вы промграли!)')
    elif gg!=n and pip!=0:
        pip-=1
        if gg<n:
            print"""Больше',
            '  -1 попытка у вас осталось'""",pip)
        elif gg>n:
            print("""Меньше','|   
            -1 попытка у вас осталось""",pip)


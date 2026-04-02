import random
print('вы попали в игру кальмара и у вас 5',' попытки угадать число')
print('от 0 до 100')
n=random.randint(1,100)
pip=5
for i in range(pip+1):
    gg=int(input('введите предпологаемое число  '))
    if gg==n and pip!=0:
        print('вы выйграли 456 милиардов вон')
        break
    elif gg!=n and pip==0:
        print('у вас закончились попытки и')
        print('вы отправляетесь на остров эпштена:)')
    elif gg!=n and pip!=0:
        pip-=1
        if gg<n:
            print('больше','|   -1 попытка у вас осталось',pip)
        elif gg>n:
            print('меньше','|   -1 попытка у вас осталось',pip)

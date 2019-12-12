import math

arr = ['&', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У',
       'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', ' ', '1', '2', '3', '4', '5', '6', '7', '8', '9',
       '0']


def rsa(p, q, text):
    slov = []
    for i in text:
        i = i.title()
        slov.append(arr.index(i))

    print(slov)

    n = p * q
    print(f'n = {n}')
    f = (p - 1) * (q - 1)
    print(f'f = {f}')
    for i in range(1, 100):
        if f % i == 0:
            pass
        else:
            e = i
            print(f'e = {e}')
            break
    k = 0
    for i in range(1, 100):
        if ((i * f + 1) / e) % 1 == 0:
            k = i
            print(f'k = {k}')
            break
        else:
            pass
    d = math.ceil((k * f + 1) / e)
    print(f'd = {d}')
    itog = []
    for i in slov:
        i = math.ceil((i ** e) % n)
        itog.append(i)
    itog = str(itog)
    itog = itog.replace(',', '')
    itog = itog.replace(']', '')
    itog = itog.replace('[', '')
    print(itog)


def obr_rsa(d, n, shifr):
    itog = []
    for i in shifr:
        i = (i ** d) % n
        itog.append(arr[int(i)])

    print(''.join(map(str, itog)))


while True:
    print('1: Шифровка')
    print('2: Расшифровка')
    s = int(input('Сделайте выбор: '))
    if s == 1:
        text = str(input('Введите текст: '))
        print('p и q должны быть простыми')
        p = int(input('Введите значение p: '))
        q = int(input('Введите значение q: '))
        rsa(p, q, text)
    else:
        shifr = [int(i) for i in input('Введите зашифрованные коды через пробел: ').split()]
        d = int(input('Введите значение d: '))
        n = int(input('Введите значение n: '))
        obr_rsa(d, n, shifr)

import math

arr = ['&', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У',
       'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', ' ', '1', '2', '3', '4', '5', '6', '7', '8', '9',
       '0']

try:
    def encryption_rsa(p, q, text):
        kod = [arr.index(i.title()) for i in text]
        print(kod)

        n = p * q
        print(f'n = {n}')

        f = (p - 1) * (q - 1)
        print(f'Функция Эйлера f = {f}')

        for i in range(1, 1000):
            if f % i != 0:
                e = i
                print(f'e = {e}')
                break

        for i in range(1, 1000):
            if ((i * f + 1) / e) % 1 == 0:
                k = i
                print(f'k = {k}')
                break

        d = math.ceil((k * f + 1) / e)
        print(f'd = {d}')

        # Начинаем шифровать сообщение
        encryption = str([(i ** e) % n for i in kod])
        encryption = encryption.replace(
            ',', '').replace(']', '').replace('[', '')
        print(f'Закртытое сообщение: {encryption}')

    def decryption_rsa(d, n, text):
        decryption = [arr[(i ** d) % n] for i in text]
        print(''.join(map(str, decryption)))

    while True:
        print("1: Шифровка\n2: Расшифровать")
        choice = int(input("Сделайте выбор: "))
        if choice == 1:
            text = str(input('Введите текст: '))
            print('p и q должны быть простыми')
            p = int(input('Введите значение p: '))
            q = int(input('Введите значение q: '))

            # Проверка на простоту по теореме Вильсона
            if (math.factorial(p - 1) + 1) % p != 0 or (math.factorial(q - 1) + 1) % q != 0:
                print("Числа должны быть простыми")
                continue
            else:
                encryption_rsa(p, q, text)
        else:
            text = [int(i) for i in input(
                'Введите закртытое сообщение через пробел: ').split()]
            d = int(input('Введите значение d: '))
            n = int(input('Введите значение n: '))
            decryption_rsa(d, n, text)

except Exception as e:
    print("Моей вины здесь нет\nпопробуйте числа больше")

import random

min_value = 1
max_value = 100

number = random.randint(min_value - 1, max_value + 1)

print(f'Угадайте целое число от {min_value} до {max_value}!')

while True:
    answer = input('Угадайте число: ')
    if answer == "" or answer == "exit":
        print("Выход из программы")
        break

    if not answer.isdigit():
        print("Введите правильное число")
        continue

    answer = int(answer)

    if answer == number:
        print('Совершенно верно!')
        break

    elif answer < number:
        print('Загаданное число больше')
    else:
        print('Загаданное число меньше')

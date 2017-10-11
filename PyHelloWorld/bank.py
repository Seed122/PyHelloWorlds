#Пользователь делает вклад в размере a рублей сроком на years лет под 10% годовых 
#(каждый год размер его вклада увеличивается на 10%. Эти деньги прибавляются к сумме вклада, и на них в следующем году тоже будут проценты).

#Написать функцию bank, принимающая аргументы a и years, и возвращающую сумму, которая будет на счету пользователя.

percentage = 0.1

def bank(deposit, years):
    sum = deposit
    for i in range(0, years): #верхняя граница range - не включается!
        sum += sum*percentage
    return sum

def clearScreen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    
    clearScreen()
    print("Введите депозит (или пустую строку для выхода)")
    s = input()
    if s=='':
        break
    deposit = int(s)
    print("Введите количество лет")
    s = input()
    if s=='':
        break
    years = int(s)

    print("Итоговая сумма: {0} руб при ставке {1}%".format(bank(deposit, years), percentage*100))
    print("Введите что угодно для продолжения")
    s = input()
# Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000, и возвращающую True, если оно простое, и False - иначе.

def check_number(number:int):
    if(number < 0 or number > 1000):
        raise ValueError("Значение должно быть в пределах от 0 до 1000")

def is_prime(number):
    check_number(number)
    for i in range(2, number):
        if((number%i)==0):
            return False
    return True

def is_prime2(number: int):
    """Возвращает 0, если число простое, и его наименьший множитель, если непростое
    """
    check_number(number)
    for i in range(2, number//2+1):
        if((number%i)==0):
            return i
    return 0

while True:
    s = input()
    if s=='':
        break
    number = int(s)
    #print("{0} {1}".format(number, "простое" if is_prime(number) else "(блин, а как такие числа называются?)"))
    try:
        mul = is_prime2(number)
    except ValueError as e:
        if(len(e.args) > 0):
            print(e.args[0])
        continue
    print("{0} {1}".format(number, "простое" if mul==0 else "непростое. Наименьший множитель - {}".format(mul)))

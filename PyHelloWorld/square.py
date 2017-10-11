# Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа): периметр квадрата, площадь квадрата и диагональ квадрата.
def calculate_square(side):
    return (side*4, side**2, (2*side**2)**(1/2))


while True:
    s = input()
    if s=='':
        break
    side = float(s)
    (perimeter, square, diagonal) = calculate_square(side)
    print("Perimeter: {0}, Square: {1}, Diagonal: {2}".format(perimeter, square, diagonal))
# Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный, и False иначе.
def is_year_leap(year):
    if((year%4 == 0) & (year%100 != 0) | (year%400 == 0)):
        return True
    return False


def print_leap_year(year):
    leap = is_year_leap(year)
    print("Год {0} {1}".format(year, "високосный" if leap else "невисокосный"))
    #if(leap):
    #    print("Год "+str(year)+" високосный")
    #else:
    #    print("Год "+str(year)+" невисокосный")


#for year in range(2010, 2030):
#     print_leap_year(year)

while True:
    s = input()
    if s=='':
        break
    year = int(s)
    print_leap_year(year)
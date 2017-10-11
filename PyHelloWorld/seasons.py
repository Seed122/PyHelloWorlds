# Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень).
def get_season(month):
    if(month>=1 and month<=2 or month==12):
        return "зима"
    elif(month >= 3 and month <= 5):
        return "весна"
    elif(month >= 6 and month <= 8):
        return "лето"
    elif(month >= 9 and month <= 11):
        return "осень"
    return "это не месяц"

for month in range(-1, 20):
    print("Месяц: {0}, сезон: {1}".format(month, get_season(month)))
import random

def rnd():
    return random.randint(-99999999000000000,99999999000000000)

def print_hello():
    print("Hello world from module. Random is {}", rnd())
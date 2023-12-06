# Aquí programa una función que resuelva el problema 1 FizzBuzz
def fizzbuzz():
    for a in range(1, 101):
        if a % 3 == 0 and a % 5 == 0:
            print("fizzBuzz")
        elif a % 5 == 0:
            print("Buzz")
        elif a % 3 == 0:
            print("Fizz")
        else:
            print(a)


fizzbuzz()

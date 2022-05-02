#Afficher nombres de 1 à 100
#Si nombre divisible par 3 => Fizz
#Si nombre divisible par 5 => Buzz
#Si nombre divisible par 3 & 5 => FizzBuzz

for i in range(1, 101):
    divisible_3 = ((i % 3) == 0)
    divisible_5 = ((i % 5) == 0)

    if divisible_3 and divisible_5:
        print("FizzBuzz")
    elif divisible_3:
        print("Fizz")
    elif divisible_5:
        print("Buzz")
    else:
        print(i)

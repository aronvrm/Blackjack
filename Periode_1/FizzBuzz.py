from time import sleep


for fizzbuzz in range(51):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("Fizzbuzz")
        continue

    elif fizzbuzz % 3 == 0:
        print("Fizz")
        continue

    elif fizzbuzz % 5 == 0:
        print("Buzz")
        continue

    else:
        print(fizzbuzz)

    sleep(0.5)


print(fizzbuzz)

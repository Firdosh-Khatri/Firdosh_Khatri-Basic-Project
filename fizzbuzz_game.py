print("This is the code for fizz buzz for the multiples of 10 and 5")
for i in range(1001):
    if (i % 10 == 0 and i % 5 == 0):
        print("FizzBuzz")
    elif (i % 10 == 0):
        print("Fizz")
    elif (i % 5 == 0):
        print("Buzz")
    else:
        print(i)
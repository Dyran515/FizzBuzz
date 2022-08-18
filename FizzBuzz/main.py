for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:     # Is number divisible by 3 and 5
        print("FizzBuzz")                           # Then print "FizzBuzz"
    elif number % 3 == 0:                       # Is number divisible by 3
        print("Fizz")                               # Then print "Fizz"
    elif number % 5 == 0:                       # Is number divisible by 5
        print("Buzz")                               # Then print "Buzz"
    else:
        print(number)                           # Else print the number
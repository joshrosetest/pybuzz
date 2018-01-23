import sys

def fizzbuzz():
    if(len(sys.argv) > 1):
        value = sys.argv[1]
        try:
            value = int(value)
            if(value % 3 == 0 and value % 5 == 0):
                print("FizzBuzz")
            elif(value % 3 == 0):
                print("Fizz")
            elif(value % 5 == 0):
                print("Buzz")
            else:
                print(value)
        except ValueError:
            print("Argument must be a valid number")
    else:
        print("A number argument is required")

fizzbuzz()

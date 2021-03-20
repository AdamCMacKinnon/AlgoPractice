
numbers = range(1,100)

def fizzbuzz(numbers):
    for num in numbers:
        if num % 3 == 0 and num % 5 == 0:
            print('fizz_buzz')
        elif num % 3 == 0:
            print('fizz')
        elif num % 5 == 0:
            print('buzz')
        
        else:
            print(num)

print(fizzbuzz(numbers))









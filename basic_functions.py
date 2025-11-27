

def add(num1, num2):

    return num1 + num2
    pass  # Implement addition

def subtract(num1, num2):

    return num1 - num2
    pass  # Implement subtraction

def multiply(num1, num2):

    return num1 * num2
    pass  # Implement multiplication

def divide(num1, num2):
    if num2 == 0:
        raise ValueError
    
    else:
        return num1 / num2
    
    pass  # Implement division with zero division check

def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return number 
    pass  # Implement FizzBuzz logic

def fibonacci(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1 
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    


    pass  # Implement Fibonacci sequence logic
        
def triangle(n):

    traingle_list = []

    for n in range(1,n + 1):
        # if n == 0:
        #     return []
        num_stars = 2* n - 1
        star_string =  num_stars * "*"
        traingle_list.append(star_string)
    
    return  traingle_list
    pass  # Implement triangle generation logic
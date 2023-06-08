def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def summation(n):
    if n == 1:
        return 1
    return n + summation(n-1)

def sum_odd(list):
    if len(list) == 0:
        return 0
    if list[0]%2 != 0:
        return list[0] + sum_odd(list[1:])
    else:
        return sum_odd(list[1:])

def sum_sub(list):
    if len(list) == 0:
        return 0
    if list[0]%2 != 0:
        return list[0] + sum_sub(list[1:])
    else:
        return -list[0] + sum_sub(list[1:])

    


# factorial(4)
# fibonacci(7)
# summation(8)
# sum_odd([1,2,3,4,5,7])
sum_sub([1,2,3,4])
n = int(input())

def factorial(n):
    m = n -1

    for i in range(n-1):
        n = n * (m)
        m -= 1
    return n
    
print(factorial(n))
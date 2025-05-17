#Lo mismo que con FizzBuzz
num = int(input())

def juego(num):
        if num % 3 == 0 and num % 5 == 0:
                return "es divisible por 3 y 5"
        
        elif num % 3 == 0:
                return "es divisible por 3"
        
        elif num % 5 == 0:
                return "es divisible por 5"
        
print(juego(num))
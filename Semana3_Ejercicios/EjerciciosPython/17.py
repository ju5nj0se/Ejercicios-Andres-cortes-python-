import time
i = 10
while i != 0:
    print(i)
    time.sleep(1)
    i -= 1
print("\033[91m" + "KABOOOM!!" + "\033[0m")
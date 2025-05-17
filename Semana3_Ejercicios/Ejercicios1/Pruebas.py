import random

flag = True
while flag:
    opt = input("Enter para girar la ruleta\n>>")

    if opt == "":
        a = random.choice(["A", "B", "C"])
        b = random.choice(["A", "B", "C"])
        c = random.choice(["A", "B", "C"])
        if a == b and a == c:
            print("Ganaste!!")
            exit()
        else:
            print("Intentanlo de nuevo :(")
    
    else:
        flag = False

    
    

    


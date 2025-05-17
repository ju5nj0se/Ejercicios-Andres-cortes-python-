flag= True
while flag:
    calificacones= int(input())

    if calificacones in range(1, 11):
        break
    else:
        print("CALIFICACION DE 1 - 10")

if calificacones >= 6:
    print("aprobatoria")
elif calificacones < 6:
    print("no es aprobatoria")
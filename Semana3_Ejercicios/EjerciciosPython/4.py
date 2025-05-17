edad=int(input())

if edad < 13:
    print("niño")

elif edad in range(13, 18):
    print("adolescente")
elif edad in range(18,50):
    print("es adulto")
elif edad >= 50:
    print("es anciano")
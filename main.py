def Degree(a,b):
    if b == 0:
        return 1
    else:
        return a * Degree(a,b-1)

a = int(input("Введите число"))
b = int(input("Введите в какую степень возвести число"))

print(Degree(a,b))
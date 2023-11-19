i = int(input("ingrese su dividendo: "))
n = int(input("ingrese su divisor: "))


def division_con_restas(i, n):
    if i < n:
        return 0
    else:
        i = i - n
        return 1 + division_con_restas(i, n)


resul = division_con_restas(i=i, n=n)
print(f"el resultado de su division es: {resul}")

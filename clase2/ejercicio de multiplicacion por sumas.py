"""
calcular una multiplicacion con sumas
"""
i = int(input("ingrese su multiplicando: "))
n = int(input("ingrese su multiplicador: "))


def multipli_con_sumas(i, n):
    if n == 0:
        return 0
    else:
        return i + multipli_con_sumas(i, n - 1)


resul = multipli_con_sumas(i=i, n=n)
print(resul)

"""
resul = multipli_con_sumas(5, 3)
print(f" su multiplicacion es {resul}")
"""


import random

lista_num = []
for i in range(10):
    lista_num.append(random.randint(1,100))

lista_invertida = lista_num[::-1]
print("original", lista_num)
print("invertida", lista_invertida)

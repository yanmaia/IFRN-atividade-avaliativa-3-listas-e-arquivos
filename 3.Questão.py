import random,sys
n=int(input("Informe o tamanho da lista deve ser entre 7 e 60: "))
if  n< 7 or n> 60:sys.exit("Informe um tamanho entre 7 e 60")

#list=[random.randint(1,61) for _ in range (n)]
lista= list()
contador=1
while contador <= n:
    valor=random.randint(1,60)
    if valor not in lista:
        lista.append(valor)
        contador+=1
print(lista)
comb=[]
for i in lista:
    print(i)
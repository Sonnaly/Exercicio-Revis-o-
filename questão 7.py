lista1 = []
lista2 = []

for i in range(1,11):
  list1 =  int(input("Digite um numero impar em um vetor X[%d]: "%(i)))
  print("")
  list2 =  int(input("Digite um numero par em um vetor X[%d]: "%(i)))
  print("")

  lista1.append(list1)
  lista2.append(list2)

vetor_composto = []

for i in range(10):
  a = lista1[i]
  b = lista2[i]

  vetor_composto.append(a)
  vetor_composto.append(b)

print (vetor_composto)

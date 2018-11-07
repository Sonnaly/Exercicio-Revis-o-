notas = 0
lista = []
lista_reversa = []
while True:
  notaX= int(input("Digite uma nota: "))

  if notaX == -1:
    break
  
  notas += 1
  lista.append(notaX)
  lista_reversa = lista[::-1]

print("")
print(" A quantidade valores lidos foi: %d\n"%(notas))

print(" Os valores na ordem que foram informados:")
for i in range(len(lista)):
  print(lista[i], end = " ")

print("")

print("")
print(" Os valores na ordem inversa que foram informados um abaixo do outro:")
for j in range(len(lista_reversa)):
  print(lista_reversa[j], end = " ",)
  print("")

print("")
somaVetor = 0
for k in range(len(lista)):
  somaVetor += lista[k]

print(" A soma dos valores dos elementos do vetor é: %d\n" %(somaVetor))
print(" A media dos valores do elementos do vetor é: %d\n"%(somaVetor/len(lista)))

acimaMedia = 0
for l in range(len(lista)):
  if lista[l] > somaVetor/len(lista):
    acimaMedia +=1

print(" A quantidade de valores acima da media é: %d\n"%(acimaMedia))

abaixoSete = 0
for m in range(len(lista)):
  if lista[m] < 7:
    abaixoSete+=1

print(" A quantidade de valores abaixo de sete é: %d\n"%(abaixoSete))

print(" FIM!") 

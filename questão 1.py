n1=int(raw_input())
n2=int(raw_input())
n3=int(raw_input())
media=(n1+n2+n3)/3
if(media < 7):
  print("reprovado")
elif(media > 7):
  print("aprovado")
elif(media==10):
  print("aprovado com distinção")

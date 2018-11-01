cont = 0
p1=raw_input('Telefonoou para vitima')
p2=raw_input('esteve no local do crime')
p3=raw_input('mora perto da vitima')
p4=raw_input('Devia para vitima')
p5=raw_input('Já trabalhou para vitima')
if(p1=='sim'):
  cont+=1
if(p2=='sim'):
  cont+=1
if(p3=='sim'):
  cont+=1
if(p4=='sim'):
  cont+=1
if(p5=='sim'):
  cont+=1

if(cont==2):
  print("Suspeita")
elif(cont==3 or cont== 4):
  print("Cumplice")
elif( cont==5):
  print("assassina")
else:
  print("inocente")  





 


Tuple=[(1,2),(3,5),(7,8)]
l2=[]
l3=[]

for each in Tuple:
  l1=each[0]+each[1]
  l2.append(l1)
  l3=tuple(l2)
print(l3,type(l3))

      
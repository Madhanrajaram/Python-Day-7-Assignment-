Mixed=[(1,2,3),[1,2],["a","hit","less"]]
a=[]
b=[]
c=[]
for i in Mixed:
    if type(i)==tuple:
        a=list(i)
    if type(i)==list:
        b=b+i
c=a+b
print(c)
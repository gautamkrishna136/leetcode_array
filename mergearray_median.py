import statistics as st
k=[]
o=[]

a=int(input("enter the len for the first list:--"))
b=int(input("enter the len for the second list:--"))
for t in range(0,a):
    a1=int(input("enter the first list element:--"))
    k.append(a1)
for n in range(0,b):
    a2=int(input("enter the second list element:--"))
    o.append(a2)
m=k+o
med=st.median(m)
print("here the median:",med)




sep = []
for i in range(0,10):
    a = input()
    sep.append(a)
    
lst =[]
for i in range(len(sep)):
   sep[i]=sep[i].lower()
   


for i in sep:
    a=i.capitalize()
    lst.append(a)
    
for i in lst:
    print(i)



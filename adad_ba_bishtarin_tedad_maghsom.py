def tedad_maghsom(adad):
    
    count = 0
    for i in range(1,adad+1):
        if adad % i == 0:
            count = count + 1
        else:
            continue  
    return count

max1 = 0    

for i in range(0,20):
    a = int(float(input()))
    b = tedad_maghsom(a)
    
    if b > max1:
        temp = b
        max1 = temp
        max_adad = a
    elif b == max1 and a>max_adad:
        
        temp = a
        max_adad = temp
        
         
    else:
        continue

print(max_adad, max1)

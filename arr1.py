a = [1, 3, 2, 4, -5]
max_val = a[0] 
count = 1 
for i in a[1:]:  
    if i > max_val:
        max_val = i
        count += 1  

print(count)

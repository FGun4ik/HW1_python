k = int(input())          
m = int(input())        
n = int(input())        
if k >= n:     
    time = m*2
else:
    time = (2*n//k)*m
    if n%k != 0 and n%k != k//2:
        time += m
print(time)
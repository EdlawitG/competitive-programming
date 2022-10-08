def theaterSquare(m,n,a)
m,n,a = map(int,input().split()) 
 
if n%a == 0: 
    res1 = n//a 
else: 
    res1 = n//a+1 
 
if m%a == 0: 
    res2 = m//a 
else: 
    res2 = m//a+1 
 
print(res1*res2) 

a=list(map(int,input().split()))
for i in a:
    n=(5*(i**2)+4)**0.5
    m=(5*(i**2)-4)**0.5
    if n == n//1 or m == m//1:
        print(i,end=" ")
        

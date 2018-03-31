#l=list(map(int, input().split()))
r, c = 6,6#l[0], l[1]
a = [[5,135,848,691,472,242],[268,689,610,419,315,364],[58,703,302,737,710,263],[223,388,71,56,19,86],[87,41,91,87,96,81],[38,48,5,88,10,29]]
'''for i in range(r):
    x = []
    x = list(map(int, input().split()))
    a.append(x)'''
count = 0
for i in range(r):
    f=[]
    for j in range(c):
        if j+1<c:
            k=j+1
            while(k < c):
                if ((a[i][j] % 10) == (a[i][k] % 10) and a[i][j]%10 not in f):
                    count += 1
                k+=1
            f.append(a[i][j]%10)

print(count)

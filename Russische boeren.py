m=int(input())
n=int(input())
som=0
print(m,n)
while n!=1:
    if n%2!=0:
        som+=m
    m=m*2
    n=n//2
    print(m,n)
som+=m
print(som)

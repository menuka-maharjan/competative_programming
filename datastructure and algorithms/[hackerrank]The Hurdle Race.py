nk=input().split()
n=int(nk[0])
k=int(nk[1])
l=list(map(int,input().rstrip().split()))
x=max(l)
if((x-k)>=0):
    print(x-k)
else:
    print(0)
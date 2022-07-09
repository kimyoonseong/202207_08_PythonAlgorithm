import sys
#sys.stdin=open("A.txt","r")
#n,m=map(int,input().split()) #정n면체 정m면
#a=list(map(int,input().split()))

N=int(input())
a=list(map(int,input().split()))

def reverse(x):
    res=0
    while x>0:
        t=x%10
        res=res*10+t
        x=x//10
    return res
        
def isPrime(x):
    if x==1:
        return False
    for i in range(2,x//2+1):#절반까지만 돌면된다
        if x%i==0:
            return False
    return True



for i in a:
    k=reverse(i)
    if isPrime(k)==True:
        print(k, end=' ')


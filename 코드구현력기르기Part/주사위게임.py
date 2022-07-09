import sys
#sys.stdin=open("A.txt","r")
#n,m=map(int,input().split()) #정n면체 정m면
#a=list(map(int,input().split()))
res=0
N=int(input())
#a=list(map(int,input().split())) 이거는 [1,2,3,4,5]이런식
for i in range(N):
    tmp=input().split()          #이거는['3','3','6']이렇게 문자열로저장
    tmp.sort()
    a,b,c=map(int,tmp)
    #print(a,b,c)
    if a==b and b==c:
        money=10000+a*1000
    elif a==b or b==c or a==c:
        if a==b or a==c:
            money= 1000+a*100
        elif b==c:
            money= 1000+b*100
    else:
        money=c*100#오름차순

    if money>res:
        res=money

print(res)

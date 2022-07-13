import sys
#sys.stdin=open("A.txt","r")
#n,m=map(int,input().split()) #정n면체 정m면
#a=list(map(int,input().split()))  #   1  3   5  띄어쓰기 받아옴.,






n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
a.insert(0,[0]*n) #첫 행 0추가생성
a.append([0]*n)#마지막행 0 추가생성
for x in a:
    x.insert(0, 0)#첫열 0 추가생성
    x.append(0)#마지막열 0 추가생
 
cnt=0

for i in range(1,n+1):
    for j in range(1,n+1):
        if a[i][j]>a[i-1][j] and a[i][j]>a[i+1][j] and  a[i][j]>a[i][j+1] and a[i][j]>a[i][j-1]:
            cnt+=1
print(cnt)

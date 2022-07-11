import sys
sys.stdin=open("A.txt","r")
#n,m=map(int,input().split()) #정n면체 정m면
#a=list(map(int,input().split()))  #   1  3   5  띄어쓰기 받아옴.,




n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))


'''내가 푼 방법
q=list()
for i in a:
    q.append(i)

for j in b:
    q.append(j)
q.sort()
for k in q:
    print(k,end=" ")

'''
p1=p2=0
c=[]
while p1<n and p2<m:
    if a[p1]<=b[p2]:
        c.append(a[p1])
        p1+=1
    else:
        c.append(b[p2])
        p2+=1
if p1<n:
    c=c+a[p1:]
if p2<m:
    c=c+b[p2:]
for k in c:
    print(k,end=" ")


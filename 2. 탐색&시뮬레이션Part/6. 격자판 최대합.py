import sys
#sys.stdin=open("A.txt","r")
#n,m=map(int,input().split()) #정n면체 정m면
#a=list(map(int,input().split()))  #   1  3   5  띄어쓰기 받아옴.,

a=int(input())
q=[]
maximum=-21470000
S=0
for i in range(a):
    b=list(map(int,input().split()))
    q.append(b)

#대각
for i in range(a):
    S+=q[i][i]

if maximum<S:
    maximum=S
S=0

#행
for i in range(a):
    for j in range(a):
        S+=q[i][j]
    if maximum<S:
        maximum=S
    S=0
#열
for i in range(a):
    for j in range(a):
        S+=q[j][i]
    if maximum<S:
        maximum=S
    S=0        
print(maximum)

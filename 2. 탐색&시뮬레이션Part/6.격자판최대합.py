import sys
#sys.stdin=open("A.txt","r")
#n,m=map(int,input().split()) #정n면체 정m면
#a=list(map(int,input().split()))  #   1  3   5  띄어쓰기 받아옴.,



#내가푼방법 100점

'''
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
'''
#강의 코드
n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
largest=-2147000000
for i in range(n):
    sum1=sum2=0
    for j in range(n):
        sum1+=a[i][j]
        sum2+=a[j][i]
    if sum1>largest:
        largest=sum1
    elif sum2>largest:
        largest=sum2
sum1=sum2=0
for i in range(n):
    sum1+=a[i][i]
    sum2+=a[i][n-i-1]#이거 생각못함
    if sum1>largest:
        largest=sum1
    elif sum2>largest:
        largest=sum2
print(largest)

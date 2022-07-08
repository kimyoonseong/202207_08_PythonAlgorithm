import sys
#sys.stdin=open("A.txt","r")
#n,m=map(int,input().split()) #정n면체 정m면
#a=list(map(int,input().split()))

N=int(input())
a=list(map(int,input().split()))

max=-13123000
cnt=[]
def digit_sum(x):#10으로 나눠서 나머
    sum=0
 
    while x>0:
        sum+=x%10
        x=x//10
    return sum


for x in a:
   
    tot=digit_sum(x)
    if max<tot:
        max=tot
        res=x
print(res)       
'''
for j in a:
    p=digit_sum(j)
    if max==p:
        print(j)
첨에ㅔ 이렇게했는데 40점나옴
'''

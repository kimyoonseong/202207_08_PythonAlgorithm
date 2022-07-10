import sys
sys.stdin=open("A.txt","r")
#n,m=map(int,input().split()) #정n면체 정m면
#a=list(map(int,input().split()))

N=int(input())
'''
for i in range(N):
    s=input()
    s=s.upper()
    size=len(s)
    for j in range(size//2):
        if s[j]!=s[-1-j]:       #s[-1]은 마지막 인덱스
            print("#%d NO" %(i+1))
            break
    else:
        print("#%d YES" %(i+1))
            

'''

for i in range(N):
    s=input()
    s=s.upper()
    
    if s==s[::-1]:
        print("#%d YES" %(i+1))
    else:
        print("#%d NO" %(i+1))
    

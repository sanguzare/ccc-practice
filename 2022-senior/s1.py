n = int(input())
ans = 0
add = 0
if (n-add)%5==0:
    ans+=1
if (n-add)%4==0:
    ans+=1
for num in range(round(n/4)):
    add+=4
    if (n-add)%5==0 and (n-add)!=0:
        ans+=1
print(ans)
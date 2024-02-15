x = int(input())
together = []
for i in range(x):
    temp_arr=input().split(" ")
    together.append(temp_arr)

y=int(input())
separate = []
for i in range(y):
    temp_arr=input().split(" ")
    separate.append(temp_arr)

g=int(input())
groups = []
for i in range(g):
    temp_arr=input().split(" ")
    groups.append(temp_arr)

for group in groups:
    violations = len(groups)
    total_violations = together_violations+separate_violations
    for twos in together:
        if (twos[0] in group) and (twos[1] in group):
            together_violations-=1
    for twos in separate:
        if (twos[0] in group) and (twos[1] in group):
            separate_violations+=1
print(total_violations)
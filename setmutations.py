n = input()
s = set(map(int, input().split())) 

for _ in range(int(input())):
    args = input().strip().split()
    nw= set(map(int, input().split())) 
    eval("s." + args[0] + "(  nw  )")
print(sum(s))
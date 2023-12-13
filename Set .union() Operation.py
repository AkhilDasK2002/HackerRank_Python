# Enter your code here. Read input from STDIN. Print output to STDOUT
n1 = input()
first = set(input().split())
n2 = input()
second = set(input().split())
third = second.union(first)
print(len(third))
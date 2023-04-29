
n = int(input("enter a value"))
arr = list(map(int, input().split()))
max_element=max(set(arr))
runner_up= max([x for x in arr if x != max_element])
print(runner_up)
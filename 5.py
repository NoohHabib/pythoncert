if __name__ == '__main__':
    n = int(input("enter a number"))
    arr = list(map(int, input("Enter a spsce seperated integer:").split(",")))
    max_element=max(set(arr))
    arr = [x for x in arr if x != max_element]
    runner_up= max(arr) if arr else None
    print(runner_up)
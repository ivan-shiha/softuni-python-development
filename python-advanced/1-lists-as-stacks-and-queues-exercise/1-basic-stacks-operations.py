def basic_stack_operations():

    inpt = input().split(" ")
    N = int(inpt[0])
    S = int(inpt[1])
    X = int(inpt[2])

    integers = input().split(" ")

    stack = []

    for i in range(N):
        num = int(integers[i])
        stack.append(num)
    
    for i in range(S):
        stack.pop()

    if len(stack) == 0:
        print(0)
        return

    if X in stack:
        print(True)
    else:
        print(min(stack))

basic_stack_operations()
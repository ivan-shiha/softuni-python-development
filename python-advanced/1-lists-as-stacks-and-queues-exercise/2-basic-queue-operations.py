def basic_queue_operations():

    inpt = input().split(" ")
    N = int(inpt[0])
    S = int(inpt[1])
    X = int(inpt[2])

    integers = input().split(" ")

    queue = []

    for i in range(N):
        num = int(integers[i])
        queue.insert(0, num)
    
    for i in range(S):
        queue.pop()

    if len(queue) == 0:
        print(0)
        return

    if X in queue:
        print(True)
    else:
        print(min(queue))


basic_queue_operations()
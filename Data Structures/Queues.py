from collections import deque

# wrap queue variable in a deque class
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
# popleft is part of the deque class
queue.popleft()
print(queue)
# check if queue is empty
if not queue:
    print("empty")

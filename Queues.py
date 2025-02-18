from collections import deque

queue = deque ()

queue.append("Pizza")
queue.append("Burger")
queue.append("Fries")

print(queue.popleft())
print(queue.popleft())

print("Remaining queue:", queue)
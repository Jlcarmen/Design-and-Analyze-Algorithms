from collections import deque

stack = deque ()

stack.append("Pizza")
stack.append("Burger")
stack.append("Fries")

print(stack.pop())
print(stack.pop())

print("Stack after popping:", stack)
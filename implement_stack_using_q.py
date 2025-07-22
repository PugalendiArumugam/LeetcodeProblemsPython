# 225 Implement stack using queue
# Example 1:
# Input
# ["MyStack", "push", "push", "top", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 2, 2, false]
# Explanation
# MyStack myStack = new MyStack();
# myStack.push(1);
# myStack.push(2);
# myStack.top(); // return 2
# myStack.pop(); // return 2
# myStack.empty(); // return False
from collections import deque


class MyStack:
    def __init__(self):
        self.curr_queue=deque()
        self.temp_queue=deque()

    def push(self, x: int) -> None:
        self.temp_queue.append(x)
        while self.curr_queue:
            self.temp_queue.append(self.curr_queue.popleft())
        self.curr_queue, self.temp_queue = self.temp_queue, self.curr_queue

    def pop(self) -> int:
        return self.curr_queue.popleft()

    def top(self) -> int:
        return self.curr_queue[0]

    def empty(self) -> bool:
        return len(self.curr_queue) == 0

myStack = MyStack()
print(myStack)
print(myStack.push(1))
print(myStack.push(2))
print(myStack.top())
print(myStack.pop())
print(myStack.empty())

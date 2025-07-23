# 232 Implement Queue using stack
# Example 1:
# Input
# ["MyQueue", "push", "push", "peek", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 1, 1, false]
# Explanation
# MyQueue myQueue = new MyQueue();
# myQueue.push(1); // queue is: [1]
# myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
# myQueue.peek(); // return 1
# myQueue.pop(); // return 1, queue is [2]
# myQueue.empty(); // return false
class MyQueue:

    def __init__(self):
        self.push_stack=[]
        self.pop_stack=[]

    def push(self, x: int) -> None:
        self.push_stack.append(x)

    def pop(self) -> int:
        self._helper_stack()
        return self.pop_stack.pop()

    def peek(self) -> int:
        self._helper_stack()
        return self.pop_stack[-1]

    def empty(self) -> bool:
        return not self.push_stack and not self.pop_stack

    def _helper_stack(self):
        if not self.pop_stack:
            while self.push_stack:
                self.pop_stack.append(self.push_stack.pop())

myQueue = MyQueue()
print(myQueue)
print(myQueue.push(1))  # queue is: [1]
print(myQueue.push(2))  # queue is: [1, 2] (leftmost is front of the queue)
print(myQueue.peek())   # return 1
print(myQueue.pop())    # return 1, queue is [2]
print(myQueue.empty())  # return false

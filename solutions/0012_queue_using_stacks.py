"""
LeetCode 232: Implement Queue using Stacks
Implement a first in first out (FIFO) queue using only two stacks. 
The implemented queue should support all the functions of a normal queue 
(push, peek, pop, and empty).

Approach: Use two stacks - one for incoming elements (stack1), 
one for outgoing elements (stack2). When we need to pop/peek and stack2 is empty,
transfer all elements from stack1 to stack2.

Time Complexity: 
- push: O(1)
- pop/peek: O(1) amortized (O(n) worst case when stack2 needs refilling)
- empty: O(1)
Space Complexity: O(n) - where n is number of elements in queue
"""

class MyQueue:
    """
    Queue implementation using two stacks.
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []  # For pushing elements
        self.stack2 = []  # For popping/peeking elements

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.peek()  # Ensure stack2 has elements if needed
        return self.stack2.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        # If stack2 is empty, transfer all elements from stack1
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.stack1 and not self.stack2

# Test cases
if __name__ == "__main__":
    # Test case 1
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    print(f"After pushing 1, 2:")
    print(f"Peek: {obj.peek()}")  # Expected: 1
    print(f"Pop: {obj.pop()}")    # Expected: 1
    print(f"Empty: {obj.empty()}") # Expected: False
    print()
    
    # Test case 2
    obj = MyQueue()
    obj.push(1)
    print(f"After pushing 1:")
    print(f"Pop: {obj.pop()}")    # Expected: 1
    print(f"Empty: {obj.empty()}") # Expected: True
    print()
    
    # Test case 3 - Multiple operations
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    obj.push(3)
    print(f"After pushing 1, 2, 3:")
    print(f"Pop: {obj.pop()}")    # Expected: 1
    print(f"Pop: {obj.pop()}")    # Expected: 2
    obj.push(4)
    print(f"After pushing 4:")
    print(f"Pop: {obj.pop()}")    # Expected: 3
    print(f"Pop: {obj.pop()}")    # Expected: 4
    print(f"Empty: {obj.empty()}") # Expected: True
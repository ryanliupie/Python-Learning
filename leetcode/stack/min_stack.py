class MinStack: 
    def __init__(self): 
        '''
        we have a normal stack and a stack that tracks 
        the minimum value which will always be placed 
        on top. 
        '''
        self.stack = []
        self.min_stack = []
    
    def push(self, val: int) -> None: 
        '''
        1. simply append the values to the normal 
        stack 

        2. The condition self.min_stack[-1] < val is asking: 
        "is the current min smaller than the new value I'm about to push?". 
        For example: 
        
        min_stack[-1] = 3
        val = 5 
        3 < 5 -> True -> carry forward the old min (3)

        so now we have: 
        stack = [3, 5]
        min_stack = [3, 3]

        3. If that is not the case, simply append the next smallest value 
        '''
        self.stack.append(val)

        if not self.min_stack: 
            self.min_stack.append(val)
        elif self.min_stack[-1] < val: 
            self.min_stack.append(self.min_stack[-1])
        else:
            self.min_stack.append(val)
 
    def pop(self) -> None: 
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int: 
        return self.stack[-1]

    def getMin(self) -> int: 
        return self.min_stack[-1]

ms = MinStack()
ms.push(1)
ms.push(2)
ms.push(0)

print(ms.getMin())  # 0
ms.pop()
print(ms.top())     # 2
print(ms.getMin())  # 1
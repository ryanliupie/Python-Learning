def evalRPN(tokens) -> int: 
    operators = {
        "+", ..., 
        "-", ..., 
        "*", ..., 
        "/", ...
    }

    stack = []
    for char in tokens: 
        if char not in operators: 
            stack.append(int(char))
        else: 
            num2 = stack.pop() 
            num1 = stack.pop() # we pop 2 elements from stack | perform operation | append back to stack
            if char == "+": 
                stack.append(num1 + num2)
            elif char == "-": 
                stack.append(num1 - num2)
            elif char == "*": 
                stack.append(num1 * num2)
            else: 
                stack.append(int(num1 / num2))
        
    return stack[0]

print(evalRPN(["2","1","+","3","*"]))
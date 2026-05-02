def dailyTemperatures(temperatures: list[int]) -> list[int]: 
    stack = []
    result = [0] * len(temperatures) # result = [0, 0, 0, 0]

    for i in range(len(temperatures)): 
        while stack and temperatures[stack[-1]] < temperatures[i]: 

            index = stack.pop()
            result[index] = i - index
        stack.append(i)

    return result 

print(dailyTemperatures([30,38,30,36,35,40,28]))

''' 
                     i   
                0    1  2   3 
temperatures = [30, 60, 30, 90]; index = 0

stack = [1]

result = [1, 0, 0, 0]

'''
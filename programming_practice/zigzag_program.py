# Zig Zag Program 

import time # this module lets us add delays in the execution using time.sleep()
import sys # this helps use handle specific operations; in this case, it will be used to exit the program cleanly with sys.exit()

indent = 0 # variable helps how much space will be added before printing asterisks 
indentIncreasing = True # boolean value to determine if the amount of indentation is increasing or decreasing

try: 
    while True: 
        print(' ' * indent, end='') # space in empty string, so it is not an empty string anymore. It will multiply the indent to create more spaces. end='' prints out spaces before printing the next line. 
        print('********')
        time.sleep(0.1) # before printing the next line, we will pause of a 1/10 of second 

        if indentIncreasing: # if the indent is increasing, we move ******** to the right and once it reaches 20  indents, it will move to the right 
            indent = indent + 1 
            if indent == 20: 
                indentIncreasing = False

        else:
            indent = indent - 1 # as the indent moves, it will reach zero, and once it reaches zero, the indent will start increasing, thus, moving to the right
            if indent == 0: 
                indentIncreasing = True 

except KeyboardInterrupt: # if user presses Ctrl+C at a point, python raises this exception and cleanly terminates the program 
    sys.exit()
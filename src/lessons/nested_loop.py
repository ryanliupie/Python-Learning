for e in range(4): # this outer loop executes the inner loop to run 4 times 
    for i in range(1, 10): 
        print(i, end="") # ends all values on the same line 
    print() # after each loop iteration, "print()" is called to handle the new line, then the outer loop repeatsa 2nd and 3rd time


rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))
symbol = str(input("Enter a symbol to use: "))

for i in range(rows): # takes how many rows we want or how many times we want to loop
    for y in range(columns): # specifies a range/length, so in this case a column
        print(symbol, end="")
    print()


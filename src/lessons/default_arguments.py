# Default Arguments: Instead of passing 3 arguments for 3 parameters, we can set some of the parameters to a specific number instead of calling it.
import time
def net_price(list_price, discount=0, tax=0.13):
    return list_price * (1 - discount) * (1 + tax)

print(net_price(500))
print(net_price(500, 0.1)) # now instead of using discount of "0", the function will use 0.1

def count(end, start=0): #notice how this is reversed? non-default arguments must be set before default arguments
    for x in range (start, end+1):
        print(x)
        time.sleep(0.7)
    print("Done!")

count(10)

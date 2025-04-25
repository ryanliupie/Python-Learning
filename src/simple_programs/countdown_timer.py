# Creator: Ryan Liu
# 04/25/2025
# Countdown Timer

import time 

try: 
    my_time = int(input("Enter a time in seconds (whole number): "))
    while my_time:
        for i in range(my_time, 0, -1): # [start, stop, step(down by 1 in this case)]
            print(i)
            time.sleep(1)
        print("The time is up!!")
        my_time = int(input("Enter another time in seconds: "))

except ValueError:  
    print("You did not enter the correct value. Please try again.")





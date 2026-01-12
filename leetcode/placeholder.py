s = "([{}])"

list1 = []

for c in s:
    list1.append(c)

l = 0 
r = len(list1) - 1 



while (l < r):
    if list1[l] == list1[r]: 
        l += 1 
        r -= 1 
    else: 
        print(False)
    

print(True)



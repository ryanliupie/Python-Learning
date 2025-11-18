paths = [["B","C"],["D","B"],["C","A"]]

new_list = []

for i in range(len(paths)): 
    new_list.append(paths[i][1])
print(new_list[-1])


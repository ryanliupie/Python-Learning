# Set = unordered collection of mutable data that cannot contain duplicates 

colours = {"black", "white", "red","orange"}
fruits = {"banana", "mango", "orange", "watermelon"}

#colours.update(fruits) # this adds the sets together 

#for x in colours: # each time this is ran, the order is randomized 
 #   print(x)

print(colours.difference(fruits)) #prints what colours have that fruits do not (good for comparision if sets have same values)
print(fruits.intersection(colours)) # prints what value they have in common 
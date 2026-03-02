list1 = ["animal", "animal", "mars", "mars"]

new_dict = {}

for word in list1: 
    new_dict[word] = new_dict.get(word, 0) + 1 

print(new_dict)
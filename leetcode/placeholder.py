def groupAnagrams(strs): 
    dict1 = dict()

    for word in strs: 
        key = tuple(sorted(word))
        
        if key not in dict1: 
            dict1[key] = []
        dict1[key].append(word)

    return list(dict1.values())

print(groupAnagrams(["act","pots","tops","cat","stop","hat"]))


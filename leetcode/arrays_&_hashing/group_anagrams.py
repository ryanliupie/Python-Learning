def GroupAnagrams(strs):
    hashmap = {}
    for word in strs: 
        key = tuple(sorted(word))
        
        if key not in hashmap: 
            hashmap[key] = []
        hashmap[key].append(word)
    
    return list(hashmap.values())

print(GroupAnagrams(["act","pots","tops","cat","stop","hat"])) 
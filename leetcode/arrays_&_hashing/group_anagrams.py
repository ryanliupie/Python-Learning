def GroupAnagrams(strs):
    hashmap = {}
    for word in strs: 
        key = tuple(sorted(word))
        hashmap[key] = hashmap.get(key, []) + [word]
    
    return list(hashmap.values())

print(GroupAnagrams(["act","pots","tops","cat","stop","hat"])) 
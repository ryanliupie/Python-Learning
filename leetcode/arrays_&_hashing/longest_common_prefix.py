def longestCommonPrefix(strs): 
    prefix = strs[0]
    for i in range(len(prefix)): 
        for word in strs: 
            if i == len(word) or prefix[i] != word[i]: 
                return prefix[:i]
    return prefix

print(longestCommonPrefix(["flower","flow","flight"]))
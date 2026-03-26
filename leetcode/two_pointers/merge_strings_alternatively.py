def mergeAlternatively(word1, word2): 
    i = j = 0 
    merged = ""

    len_w1 = len(word1)
    len_w2 = len(word2)

    while (i < len_w1) and (j < len_w2): 
        merged += word1[i] + word2[j]
        i += 1 
        j += 1

    if i < len_w1: 
        merged += word1[i:]
    else: 
        if j < len_w2: 
            merged += word2[j:]

    return merged 

    # w1 = ab
    # w2 = abcdefg

    # i = 0 | len(word1) = 2
    # j = 0  | len(word2) = 7 

    # 1) merged = "aa", 2) merged = "aabb" --> the loops stops since index 0 and 1 = ab which = 2 and so the len of that word is 2, the "AND" does not hold.

    # We then go to the if and else block add the rest of the values onward from that index. 

print(mergeAlternatively("ab", "abcdefg"))
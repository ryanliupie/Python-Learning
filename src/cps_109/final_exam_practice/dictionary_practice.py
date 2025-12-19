def count(nums): 
    """
    Count how many times each number appears in a list. 
    so the key = number and the values = how many times it occurs. 
    
    input: nums = [1, 2, 2, 3, 1, 2]

    output: {1: 2, 2: 3, 3: 1}

    """
    dict1 = dict()
    for num in nums: 
        dict1[num] = dict1.get(num, 0) + 1 
    return dict1
print(count([1, 2, 2, 3, 1, 2]))

#-------------------------------------------------------------------

def group(words):
    """
    Take a list of words and group it by their first letter. 
    
    input: words = ["apple", "air", "banana", "book", "cat", "car"]

    output: {
            "a": ["air", "apple"],
            "b": ["banana", "book"],
            "c": ["car", "cat"]
            }
    """
    dict2 = {}
    for word in words: 
        if word[0] not in dict2: 
            dict2[word[0]] = []
        dict2[word[0]].append(word)
        
    for key in dict2.keys():
        dict2[key] = sorted(dict2[key])
        
    return dict2

print(group(["apple", "air", "banana", "book", "cat", "car"]))

#-------------------------------------------------------------------

def count_word(words):
    """
    Give a list of words, count how many words 
    have each length. So gather the amount of length
    and make that the key. and so count how many words 
    are equal to that length. 
    
    input: words = ["hi", "dog", "cat", "yes", "a", "no"]
    
    output: {
             1: 1,   # "a"
            2: 2,   # "hi", "no"
            3: 3    # "dog", "cat", "yes"
           }

    """
    
    dict3 = dict()
    for word in words:
        dict3[len(word)] = dict3.get(len(word), 0) + 1 
    
    dict3 = dict(sorted(dict3.items()))
    return dict3
print(count_word(["hi", "dog", "cat", "yes", "a", "no"]))
        
#-------------------------------------------------------------------

def count2(words):

    """
    "Group Anagrams". take a list of words
    and group all words that are anagrams 
    of each other. 

    input: words = ["eat", "tea", "ate", "bat", "tab", "tan", "nat"]

    output: {
            "aet": ["ate", "eat", "tea"],
            "abt": ["bat", "tab"],
            "ant": ["nat", "tan"]
            }

    """
    dict1 = dict()
    for word in words: 
        x = sorted(word)
        y = "".join(x)
        
        if y not in dict1: 
            dict1[y] = []
        dict1[y].append(word)
        
    for key in dict1.keys(): 
        dict1[key] = sorted(dict1[key])
    
    return dict1
    
    
    

print(count2(["eat", "tea", "ate", "bat", "tab", "tan", "nat"]))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
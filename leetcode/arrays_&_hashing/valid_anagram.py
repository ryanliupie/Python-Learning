def ValidAnagram(s, t): 
    sort1 = sorted(s)
    sort2 = sorted(t)
    if sort1 == sort2: 
        return True
    return False
print(ValidAnagram("racecar", "carrace"))
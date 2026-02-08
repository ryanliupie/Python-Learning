def numUniqueEmails(emails): 
    set1 = set()

    for email in emails: 
        first, last = email.split("@")
        if "+" in first: 
            first = first[:first.index("+")]
        set1.add(first.replace(".", "") + "@" + last)
    
    return len(set1)


print(numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))


list1 = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]

for email in list1: 
    t, v = email.split("@") # pretty cool. so we split it at the "@" into two strings. ONLY works if there are 2 components only before the @ and after
    print(t, v)             # if we only hade "t = email.split('@')", we would get a list of those components. 
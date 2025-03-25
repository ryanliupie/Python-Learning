import re 

text = '''
Name: Ryan Liu 
Phone: 647-123-4533
Email: ryan_turbo@gmail.com
Website: https://ryanturbo.edu

Name: Bob Charles
Phone: 905-123-4537
Email: bob_charles@gmail.com
Website: https://bobcharles.edu
'''

name_pattern = re.compile(r"\b[A-Z][a-z]+\s[A-Z][a-z]+\b") # finds word with a single upper and the rest lower. IMPORTANT "[A-Z][a-z]+" the "+" attaches to the before statement and quantifies to find lower case numbers one or more times
phone_pattern = re.compile(r"\b\d{3}-\d{3}-\d{4}\b") # matches a phone number with the pattern 3 3 4. the "-" is needed to match
email_pattern = re.compile(r"\b[\w.-]+@[\w.-]+[\.\w{2,}]") # match values \w [a-zA-Z0-9_] and include .-   --> then match @ symbol with the same criteria  -->  lastly, find a literal dot (.) hence the \. then find a word character that has 2 or more characters {2,}
website_pattern = re.compile(r"https?://[\w.-]+[\.\w{2,}]") # the "?" helps match both http and https 


# ----search() find first match----

print("First name found: ", name_pattern.search(text).group())
print("First phone number found: ", phone_pattern.search(text).group())
print("First Email found: ", email_pattern.search(text).group())
print("First Website found: ", website_pattern.search(text).group())

# ----match() from the very beginning position 0----
print("First occurence: ", name_pattern.match(text))

# ----findall() finds every value in pattern---
print("All names found: ", name_pattern.findall(text))
print("All phone numbers found: ", phone_pattern.findall(text))
print("All emails found: ", email_pattern.findall(text))
print("All websites found: ", website_pattern.findall(text))

# ----finditer() like findall but more control----
# find the name of the person and their associated website

names = list(name_pattern.finditer(text)) # list of match objects for names (stored as a list to combine them later)
websites = list(website_pattern.finditer(text)) # list of match objects for websites (stored as a list to combine them later)

print("Matched Name and Website:")

for name_match, website_match in zip(names, websites): # zip combines two lists together into a tuple
    print(f"Name: {name_match.group()}") # when we just those methods above, we get a match object, not a string. .group() lets you extract the matched string from that matched object
    print(f"Website: {website_match.group()}")

# ----findsub() replaces matches----

hidden_text = email_pattern.sub("[Email Hidde]", text) # [] is apart of the string, no meaning, maskes it easier for person to see it as "hidden"
hidden_text = phone_pattern.sub("[Phone number hidden]", hidden_text) # chained replacement first email then phone. Do one first then the other

print("Hidden texts: \n")
print(hidden_text)

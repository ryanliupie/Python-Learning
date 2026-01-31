import re


text = "Hello my name is Ryan"

pattern = re.compile(r"Ryan$")

search1 = pattern.search(text)

print(search1)

print(text[17:21])
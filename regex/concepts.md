## Regular Expressions 

This is a way to search for patterns in strings or extract data from a string that follows a specific pattern. In Python, we must use `import re` module to do so. 

<b>re.compile()</b> → creates a Pattern object. Basically, this holds the pattern you are trying to look for. This Pattern object has regex methods such as `search`, `match`, `findall`, `finditer` and more! 

- You usually have to make sure to input a <b>Raw String</b> if you dealing with strings with slashes. We can use an `r` before the string. For instance if you did `\tTab` or `\nCar`, Python will interpret these as escape sequences. 

### Meta Characters

These are special characters in regex that need to be escaped if we are searching for them. This is because if we do not escape it, regex will do special things with them. 

- `.` → matches any single character in between a string. For example if we have <b>r"a.c"</b>, that dot can be `aZc`, `a c`, `a/c`, `a3c`. 

- `^` → matches the start of the string at index 0. For example if we have <b>r"^hi"</b> at index 0, we would get `<re.Match object; span=(0, 2), match='hi'>`. This happens for every search pattern, and if we want to get the actual value, we can either index by doing `print(matches[0, 2])` or simply do `print (matches.group())`. 

- `$` → matches the end of the string. For example, if we have <b>r"Ryan$"</b>, and the text is `Hello my name is Ryan`, we would get the out of Ryan or where its index is. 

- `*` → 


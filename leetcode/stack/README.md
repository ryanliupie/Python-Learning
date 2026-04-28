## Stack 

<b>What is it?</b>

It is a type of data structure used to access and organize data in a `LIFO` or `Last In, First Out` order. 

I think of a stack like a barbell. When we put on 45lb weights, and then take them off at the end, what comes out first? The last plate that was put on comes out first. 

Specifically in Python, a regular `list` works as a stack: 

```python
stack = []

stack.append(1) # push → [1]
stack.append(500) # push → [1,500]
stack.append(1200) # push → [1,500, 1200]

stack.pop() # pops 1200 off as that was the most recent
```

When dealing with questions where a stack can be implemented, usually the `.pop()` method is used as well as `.append()`. 

<b>When to use it</b>

It is used when the most recently seen element is the one you need to do something with next. Some common patterns include: 

- <b>Matching pairs</b> → parenthesis "()", brackets "[]", braces "{}"
- <b>Undo operations</b> →  last action is the first to undo
- <b>Backtracking</b> → retracing the most recent step


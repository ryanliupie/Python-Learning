## Unit 3

### Previous Review 
<hr>

- `max()` --> This will give us the maximum number 
- `min()` --> TRhis will give us the minimum number 
- `len()` --> This gives us how long a given set of numbers or string is. Remember that it starts at index 1. For example, if the string is `Toronto`, the output would be `7`. 
- `sort()` --> This is a type of list method that orders alphabetically or smallest to greatest. 

#### Review of Strings: 
- Remember that strings are `immutable`, where we cannot alter it once we store it in memory. 
- We can `slice` strings using `[start : stop : step]`.
    
    ``` python
    word = "abcdefghi"
    word[0:3] # abc --> remember it always starts at specified value but doesn't include ending value!! 

    word = "abcdefghi"
    word[0:3:2] # ac --> this will index 'abc', but skip the second value since we specified the skip. so "1, 2(skip) = a, b(skip), c, result = ac"
    
    ```
- We can also get the `len()` of the string, index using `[]` to get the specific value we want, and concatenate them with `+`. 


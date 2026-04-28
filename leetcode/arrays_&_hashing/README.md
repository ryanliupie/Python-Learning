## Array and Hashing 

First and foremost "hashing" refers to the underlying mechanism; a <b>hash function</b> converts a key into an index in memory, allowing for `O(1)` lookups. 

We can say: 

- <b>Hash function</b> → the algorithm that converts a key into a index in memory 
- <b>Hashmap/hash table</b> → the data structure that uses that function
- <b>Hashset</b> → same idea but you <b>only store keys</b>, no values (useful for checking "have I see this before?")
<hr>

Moving on to both arrays and hashing: 

<b>What they are | When to use it</b>

Both are different types of data structures which is used when you need to track, count, or look up items in an efficient manner. Arrays give you the raw data; a hashmap lets you store information about the data as you go. 

<b>How it works</b>

A hashmap stores key-value pairs in `O(1)` time, so instead of re-scanning the array repeatedly, you build a map in one pass and look up values instantly. 

Common patterns include: 

- <b>Frequency count</b> → count how many times each value appears 
- <b>Seen before?</b> → check if you have already encountered a value 
- <b>Group/sort by value</b> group up items together by some property. Think of questions such as the "Group Anagrams" leetcode question. 

When I count items, I follow this block of code: 

```python
nums = [1, 2, 3, 3, 4, 4, 6, 7, 7]

count = {}
for num in nums: 
    count[num] = count.get(num, 0) + 1 
 ```
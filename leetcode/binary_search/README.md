## Binary Search

<b>When to use it</b> 
- It is a algorithmic technique used when the input is <b>sorted</b> (ascending or descending order) and you need to find or calculate a specific value. 

<b>How it works</b>
- Instead of checking every element, we find the midpoint of the list and place a left pointer at index 0 and a right pointer at the end (len(input) - 1). For example, let's assume we have an ascending sorted list: 

    - If the target is <b>greater than the midpoint</b> → move the <b>left pointer up</b>
    - If the target is <b>less than the midpoint</b> → move the <b>right pointer down</b>
- This is repeated until we find the target and each step cuts the search in half, so the list keeps shrinking rapidly. 

<b>Time Complexity</b>
- `O(log n)` since the work grows slowly as input size increases. 
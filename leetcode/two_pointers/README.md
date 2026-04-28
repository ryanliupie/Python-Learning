## Two Pointers 

<b>When to use it</b>

When you have an array and need to compare or combine two values based on some condition. 

<b>Common setups</b>

- <b>Opposite ends</b>
    - Start one pointer at the left, and one pointer at the right, and move them towards each other. 
    ```python
    left, right = 0, len(arr) - 1

    while left < right:
    current = arr[left] + arr[right]
    
    if current == target:
        # found answer
    elif current < target:
        left += 1    # need bigger value → move left up
    else:
        right -= 1   # need smaller value → move right down
    ```

- <b>Same direction (two separate arrays or fast/slow)</b>
    - Both pointers start at the beginning but move at different speeds or across different arrays. 

    ```python
    arr1 = [1, 3, 5, 7]
    arr2 = [3, 5, 6, 9]

    p1, p2 = 0, 0

    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] == arr2[p2]:
            # match found
            p1 += 1
            p2 += 1
        elif arr1[p1] < arr2[p2]:
            p1 += 1
        else:
            p2 += 1

    ```


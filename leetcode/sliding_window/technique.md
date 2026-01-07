### Sliding Window

This technique is used when you are given an array or string and you are working with a contiguous subarray / substring (e.g., [2, 3, 4] from [1, 2, 3, 4], elements are in their original order and there is no skipping elements). 

That subarray is either one of two things: 

- <b>fixed (K):</b> meaning there is a K value such as "3". We have an array of [1, 2, 3, 4, 5, 6, 7] and want to compute maybe the sum of size K so "[1, 2, 3]" = 6. We might be asked "what is the "biggest sum" of size K in the entire array, and so we would move the "sliding window" to the right. 

    - <b>Window</b> moves <b>right by 1</b>: → subtract (-) <b>left</b> element → <b>add new right</b> element

- <b>Dynamic:</b> Now, the sliding window is not fixed, rather the size changes dynamically to meet a certain condition. There is usually a <b>left pointer</b>  and a <b>right pointer</b>. 

    - For instance, you <b>expand the window</b> to the right to include more elements so you move the right pointer. You would then <b>check a condition</b>, then <b>shrink the window</b> or the left pointer is moved to the right when a condition is violated. 

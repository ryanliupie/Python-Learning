def bubble_sort(list1): 
    n = len(list1)
    swapped = True 

    while swapped: 
        swapped = False # assume list is sorted. this will break while loop if the `if` statement doesn't run below
        for i in range(len(list1) - 1):
            if list1[i] > list1[i+1]:
                list1[i], list1[i+1] = list1[i+1], list1[i]
                swapped = True
        n -= 1 # this shrinks the list, since the on the first iteration `765` reaches the end and is the biggest number, so we don't need that comparison
        
    return list1

print(bubble_sort([356, 2, 6, 354, 67, 23, 765, 345]))

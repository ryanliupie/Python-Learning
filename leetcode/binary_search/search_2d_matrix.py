def searchMatrix(matrix, target):
     l = 0 
     r = len(matrix) - 1 

     while (l <= r): 
        mid = (l + r) // 2 
        row = matrix[mid] # "[10,11,16,20]"

        if target < row[0]: 
                r = mid - 1 
        elif target > row[-1]: 
                l = mid + 1 
        else: # if target in this row, then we perform the binary search 

            left = 0 
            right = len(row) - 1 

            while (left <= right): 
                middle = (left + right) // 2

                if row[middle] == target: 
                    return True 
                elif row[middle] < target: 
                    left = middle + 1 
                else: 
                    right = middle - 1 
                
            return False

     return False 
    
print(searchMatrix([[1,2,4,8],[10,11,12,13],[14,20,30,40]], 10)) 
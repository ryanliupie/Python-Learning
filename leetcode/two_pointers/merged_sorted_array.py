def merge(nums1, m, nums2, n): 
   p1 = m - 1 
   p2 = n - 1 
   insert = len(nums1) - 1 # insert pointer

   while (p1 >= 0) and (p2 >= 0): 
      n1, n2= nums1[p1], nums2[p2]
      if n1 > n2: 
         nums1[insert] = n1
         p1 -= 1 # decrement the position 
      else: 
         if n2 > n1: 
            nums1[insert] = n2
            p2 -= 1 
         insert -= 1 # decrement the position 
    
    # if there are still elements in nums2, we go into this while loop:

   while (p2 >= 0):
      nums1[insert] = nums2[p2]
      p2 -= 1 
      insert -= 1  

print(merge([10,20,20,40,0,0], 4, [1,2], 2))

#[10,20,20,40,0,0]
#          p1

#[1,2]
#  p2

'''
first iteration: 

n1 = 40, n2 = 2 --> now we compare, which ever is biggest we insert the value at the end
'''
# Write a Python function to find the maximum sum subarray of a list.
def max_sum_subarray(lst):
    max_sum = cur_sum = lst[0]
    
    for num in lst[1:]:
        cur_sum = max(num, cur_sum + num)
        max_sum = max(max_sum, cur_sum)
    
    print(max_sum)

max_sum_subarray([-2,1,-3,4,-1,2,1,-5,4])
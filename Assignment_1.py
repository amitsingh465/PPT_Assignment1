#!/usr/bin/env python
# coding: utf-8

#  **Q1.** Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# 
# You can return the answer in any order.
# 
# Example: Input: nums = [2,7,11,15], target = 9 Output0 [0,1]
# 
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]

# In[1]:


def target(arr):
    target_value = int(input('Enter the value of the Targeted Value : '))
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] + arr[j] == target_value:
                return list[i,j]
            
array = [2,7,11,15]
print(target(array))


# **Q2.** Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
# 
# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k.
# Example : Input: nums = [3,2,2,3], val = 3 Output: 2, nums = [2,2,*,*]
# 
# Explanation: Your function should return k = 2, with the first two elements of nums being 2. It does not matter what you leave beyond the returned k (hence they are underscores)

# In[2]:


def remove_element(nums, val):
    i = 0
    j = len(nums) - 1
    while i <= j:
        if nums[i] == val:
            nums[i] = nums[j]
            j = j - 1
        else:
            i = i + 1

    return i

nums = [3, 2, 2, 3]
val = 3

k = remove_element(nums, val)
print("k:", k)
print("Updated nums:", nums[:k])


# **Q3.** Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.
# 
# Example 1: Input: nums = [1,3,5,6], target = 5
# 
# Output: 2

# In[4]:


def distinct(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return [i]
    
array = [1,3,5,6] 
target_value = int(input('Enter the value of the Targeted Value : '))
print("Index = ",distinct(array,target_value))


# **Q4.** You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.
# 
# Example 1: Input: digits = [1,2,3] Output: [1,2,4]
# 
# Explanation: The array represents the integer 123.
# 
# Incrementing by one gives 123 + 1 = 124. Thus, the result should be [1,2,4]

# In[5]:


def plusOne(digits):
    digit_length = len(digits) 
    i = digit_length - 1 
    while digits[i] == 9 and i >= 0:
        i = i - 1
        
    if i == -1:
        results = [0]*(digit_length + 1)
        results[0] = 1
        return results
        
    results = [0]*(digit_length) 
    results[i] = digits[i] + 1
        
    for j in range(i-1, -1, -1):
        results[j] = digits[j]
        
    return results

digits = [1,2,3]
print(plusOne(digits))


#  **Q5.** You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# 
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
# 
# Example 1: Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3 Output: [1,2,2,3,5,6]
# 
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6]. The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1

# In[6]:


def sorted_array(num1,num2):
    a=len(nums1)
    i=0
    j=0
    while i< a:
        if n  == 0 or m==0 :
            return nums1
        if nums1[i]==0:
            nums1[i]=nums2[j]
            j+=1
        i+=1
    return sorted(nums1)

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
print(sorted_array(nums1,nums2))


#  **Q6.** Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# Example 1: Input: nums = [1,2,3,1]
# 
# Output: true
# 

# In[7]:


def distinct_element(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
             if arr[i] == arr[j]:
                    return True
    return False
    
array = [1,2,3,1]
print(distinct_element(array))


# **Q7.** Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the nonzero elements.
# Note that you must do this in-place without making a copy of the array.
# 
# Example 1: Input: nums = [0,1,0,3,12] Output: [1,3,12,0,0]
# 

# In[8]:


def Push_Zero_to_Last(arr):
    
    for i in range(len(arr)-1):
        for j in range(len(arr)-1):
            if arr[j] == 0:
                arr[j],arr[j+1] =  arr[j + 1],arr[j]
            
    return arr
    
array = [0,1,0,3,12]
print(Push_Zero_to_Last(array))


# **Q8.** You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.
# You are given an integer array nums representing the data status of this set after the error.
# 
# Find the number that occurs twice and the number that is missing and return them in the form of an array.
# 
# Example 1: Input: nums = [1,2,2,4] Output: [2,3]

# In[9]:


def repetion(arr):
    repeat = 0
    miss = 0
    for i in range(len(arr)):
        if i == len(arr)-1:
            break
        if arr[i] == arr[i+1]:
            repeat = arr[i]
        if arr[i+1] - arr[i]!= 1:
            miss = i+1
    
    return [repeat,miss]

array = [1,2,2,4]
print(repetion(array))


# In[ ]:





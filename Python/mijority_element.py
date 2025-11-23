"""Problem 11 — Majority Element

You are given an array. Return the element that appears more than n/2 times.

Example:

Input: [2,2,1,1,1,2,2]
Output: 2


💡 Hint:

Use hashmap count

OR use Boyer-Moore Algorithm (advanced technique)"""

def majorityElement(arr):
    count = {}
    for i in arr:
        count[i] = count.get(i, 0) + 1
    return max(count, key=count.get)

arr=[2,2,1,1,1,2,2]
majorityElement(arr) 

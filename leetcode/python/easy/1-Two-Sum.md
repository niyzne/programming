## Challenge

You are given an array of integers `nums` and an integer `target`, return _indices of the two numbers such that they add up to `target`_.

You may assume that each input would have **_exactly_ one solution**, and you may not use the _same_ element twice.

You can return the answer in any order.

**Example 1:**

> **Input:** `nums = [2,7,11,15], target = 9`
> **Output:** [0,1]
> **Explanation:** Because nums[0] + nums[1] == 9, we return [0, 1].

**Example 2:**

> **Input:** nums = [3,2,4], target = 6
> **Output:** [1,2]

**Example 3:**

> **Input:** nums = [3,3], target = 6
> **Output:** [0,1]

**Constraints:**

- `2 <= nums.length <= 104`
- `-109 <= nums[i] <= 109`
- `-109 <= target <= 109`
- **Only one valid answer exists.**

**Follow-up:** Can you come up with an algorithm that is less than `O(n2)` time complexity?

---
Topics

- Junior
- Array
- Hash Table

---
## Code

```python
class Solution(object):
	def twoSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
```

---
## Solution

```python
# pseudocode I've thought about
class Solution(object):
  def twoSum(self, nums, target):
    # have an empty list to store the answer

    # loop through the indexes of nums
      # loop through the indexes after the first index
        # check if the value at the first index
        # plus the value at the second index equals target
          # if true:
            # add the first and second indexes to the answer list
            # return the answer
          # continue looping and checking

    # return answer
```

---
(CHALLENGE NOT COMPLETED AS OF RIGHT NOW)


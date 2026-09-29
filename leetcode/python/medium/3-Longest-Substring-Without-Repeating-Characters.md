# 3. Longest Substring Without Repeating Characters

## Challenge

Given a string `s`, find the length of the **longest** **substring** without duplicate characters.

**Example 1:**

> **Input:** `s = "abcabcbb"`
> **Output:** 3
> **Explanation:** The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

**Example 2:**

> **Input:** `s = "bbbbb"`
> **Output:** 1
> **Explanation:** The answer is "b", with the length of 1.

**Example 3:**

> **Input:** `s = "pwwkew"`
> **Output:** 3
> **Explanation:** The answer is "wke", with the length of 3.
> Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

**Constraints:**

- `0 <= s.length <= 105`
- `s` consists of English letters, digits, symbols and spaces.

---
Topics

- Staff
- Hash Table
- String
- Sliding Window

---
## Code

```python
class Solution(object):
	def lengthOfLongestSubstring(self, s):
		"""
		:type s: str
		:rtype: int
		"""
```

## Solution

```python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        slist = ""
        longestsubstr = 0
        if len(s) == 0:
            longestsubstr = 0
        elif len(s) == 1:
            longestsubstr = 1
        else:
            for i in range(len(s)):
                if s[i] not in slist:
                    slist + s[i]
                    if len(slist) > longestsubstr:
                        longestsubstr = len(slist)
                else:
                    pass

        return len(slist)
```

---

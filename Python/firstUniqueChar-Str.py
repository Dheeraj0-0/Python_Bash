"""First Unique Character in a String

Return the index of the first character that appears only once.

Example:

Input: "leetcode"
Output: 0   ('l' is first unique)

Input: "aabb"
Output: -1   (no unique character)"""
{ # wrong
def checkunique(str):
    for i in range(len(str)):
        if i == 0:
            pass
        elif str[i] == str[0]:
            return -1
        else:
            return 0

print(checkunique("leetcode"))
print(checkunique("aabb"))

}

#short & better approach
def first_unique_char(s):
    freq = {}
    
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for i in range(len(s)):
        if freq[s[i]] == 1:
            return i

    return -1

print(first_unique_char("leetcode"))  # 0
print(first_unique_char("loveleetcode"))  # 2
print(first_unique_char("aabb"))  # -1

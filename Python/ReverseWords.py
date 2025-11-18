""" "Reverse Words in a String"

Reminder:

Input:

"  hello   world  "


Output:

"world hello"


👉 Remove extra spaces
👉 Reverse words (NOT characters)
"""

s = "  hello   world  "
words = s.split()
words.reverse()
print(" ".join(words))


#!/usr/bin/env python
# coding: utf-8

# # Problem
# 
# Given a string, determine if a permutation of the string could form a palindrome.<br>
# 
# Example 1:<br>
# Input: "code"<br>
# Output: false<br>
# 
# Example 2:<br>
# Input: "aab"<br>
# Output: true<br>
# 
# Example 3:<br>
# Input: "carerac"<br>
# Output: true

# # Brainstorm 
# 
# We see permutations, so a hash table could be helpful to reduce iterations as we don't care about the order and need quick about the presence or count of a letter in the string.

# # Solution 1
# ##### hash table and frequency check

# In[1]:


from collections import Counter
def can_permute_palindrome1(s):
    if not s:
        return True
    
    letter_count = Counter(s)
    odd_count = 0
    for value in letter_count.values():
        if value % 2 == 1:
            odd_count += 1
            if odd_count == 2:
                return False
        
    return True    


# In[ ]:


import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self.s1 = ''
        self.s2 = 'bba'
        self.s3 = 'abcbac'
        self.s4 = 'abc'

    def test_palindrome1(self):
        self.assertTrue(can_permute_palindrome(self.s1))
        self.assertFalse(find_loop1(self.head2), self.loop_node)
        

    def test_palindrome2(self):
        self.assertIsNone(find_loop2(self.head1))
        self.assertEqual(find_loop2(self.head2), self.loop_node)
        self.assertIsNone(find_loop2(self.head3))
        self.assertIsNone(find_loop2(self.head4))


if __name__ == "__main__":
    unittest.main()


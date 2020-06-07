#!/usr/bin/env python
# coding: utf-8

# Implement a trie with insert, search, and startsWith methods.
# 
# Example:<br>
# 
# Trie trie = new Trie();<br>
# 
# trie.insert("apple");<br>
# trie.search("apple");   // returns true<br>
# trie.search("app");     // returns false<br>
# trie.startsWith("app"); // returns true<br>
# trie.insert("app");<br>   
# trie.search("app");     // returns true<br>
# 
# Note:
# - You may assume that all inputs are consist of lowercase letters a-z.
# - All inputs are guaranteed to be non-empty strings.

# Approach 1: nested dictionaries

# In[ ]:





# In[ ]:


class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, word):
        """Adding a word in the trie structure."""
        t = self.trie
        for w in word:
            if w not in t:
                t[w] = {}
            else:
                t = t[w]
        t['#'] = '#'

    def search(self, word):
        t = self.trie
        for w in word:
            if w not in t:
                return False
            else:
                t = t[w]
        if '#' in t:
            return True
        return False

    def startsWith(self, prefix):
        t = self.trie
        for w in prefix:
            if w not in t:
                return False
            else:
                t = t[w]
        return True


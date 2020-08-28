"""
Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""

from typing import List
import collections

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        word_dict = {}
        ans = []
        for word in wordList:
            for i in range(len(word)):
                w = word[:i] + "*" + word[i+1:]
                word_dict[w] = word_dict.get(w, []) + [word]
        queue = collections.deque()
        visited = set()
        for i in range(len(beginWord)):
            w = beginWord[:i] + "*" + beginWord[i+1:]
            if w in word_dict:
                queue.append([w, [beginWord]])
                visited.add(w)
        while queue:
            this_visited = []
            for _ in range(len(queue)):
                w1, seq = queue.popleft()
                words = word_dict[w1]
                if endWord in words:
                    ans.append(seq + [endWord])
                else:
                    for word in words:
                        for i in range(len(word)):
                            w = word[:i] + "*" + word[i+1:]
                            if w not in visited and w in word_dict:
                                queue.append([w, seq + [word]])
                                this_visited.append(w)
            for word in this_visited:
                visited.add(word)
        return ans
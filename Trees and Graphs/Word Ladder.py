"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible 
"""

from typing import List
import collections

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_dict = {}
        for word in wordList:
            for i in range(len(word)):
                w = word[:i] + "*" + word[i+1:]
                word_dict[w] = word_dict.get(w, []) + [word]
        queue = collections.deque()
        visited = set()
        for i in range(len(beginWord)):
            w = beginWord[:i] + "*" + beginWord[i+1:]
            if w in word_dict and w not in visited:
                queue.append(w)
                visited.add(w)
        steps = 1
        while queue:
            for _ in range(len(queue)):
                pattern = queue.popleft()
                words = word_dict[pattern]
                if endWord in words:
                    return (steps+1)
                else:
                    for word in words:
                        for i in range(len(word)):
                            w = word[:i] + "*" + word[i+1:]
                            if w not in visited and w in word_dict:
                                visited.add(w)
                                queue.append(w)
            steps+=1
        return 0
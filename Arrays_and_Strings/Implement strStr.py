"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

 

Constraints:

haystack and needle consist only of lowercase English characters.

Solution : Keep 2 pointers, incrementing whenever match. If no match, reset the pointers to 0 and haystack_ptr - needle_pointer + 1
            time complexity : O(N*M) -> (If there are so many mismatches)
            Space complexity : O(1)

         KMP algo : 
         Time complexity : O(M+N)
         Space complexity : 
"""

class Solution:
    def strStr(self, haystack, needle):
        h_ptr = 0
        n_ptr = 0
        while h_ptr < len(haystack) and n_ptr < len(needle):
            if haystack[h_ptr] == needle[n_ptr]:
                h_ptr+=1
                n_ptr+=1
            else:
                #reset
                h_ptr= (h_ptr-n_ptr+1)
                n_ptr = 0
                
        if n_ptr == len(needle):
            return (h_ptr - n_ptr)
        else:
            return -1

s = Solution()
print(s.strStr("mississippi", "issipi"))
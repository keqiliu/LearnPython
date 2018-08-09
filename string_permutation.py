"""
Example 1:
Input:s1 = "ab" s2 = "eidbaooo"
Output:True
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input:s1= "ab" s2 = "eidboaoo"
Output: False
"""


class Solution(object):
    @classmethod
    def check_inclusion(cls, s1, s2):
        return s1 in s2

    @classmethod
    def get_permutation(cls, s1):
        if len(s1) == 1:
            return [s1]
        distinct_char = list(set(s1))
        permutation = []
        for char in distinct_char:
            i = s1.index(char)
            permutation += [char + x for x in Solution.get_permutation(s1[0:i] + s1[i+1:])]
        return permutation

    @classmethod
    def permutation_in_string(cls, s1, s2):
        permutation = Solution.get_permutation(s1)
        return any(map(lambda x: Solution.check_inclusion(x, s2), permutation))


t1 = "abcd"
t2 = "jteaetlkajs;kljdabcasdl;kfjaskldj"
print(Solution.get_permutation(t1))
print(Solution.permutation_in_string(t1, t2))


t1 = "aboo"
t2 = "eidboaoo"
print(Solution.get_permutation(t1))
print(Solution.permutation_in_string(t1, t2))





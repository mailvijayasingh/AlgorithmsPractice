

## Recursive Intuition: Not all correct, missing edge cases

# class Solution(object):
#     def isInterleave(self, s1, s2, s3):
#         if not s3 and not s1 and not s2:
#             return True
#         if s3 and (not s1 and not s2):
#             return False
#         if s3 and (not s1 or not s2):
#             return True
#         if len(s3) != len(s1)+len(s2):
#             return False
#         if s3 and  s2 and s1:
#             if s3[0] != s1[0] and s3[0]!= s2[0]:
#                 return False
#             if s3[0] == s1[0] and s3[0] == s2[0]:
#                 return self.isInterleave(s1[1:], s2, s3[1:]) or self.isInterleave(s1, s2[1:], s3[1:])
#             if s3[0] == s1[0]:
#                 return self.isInterleave(s1[1:], s2, s3[1:])
#             if s3[0] == s2[0]:
#                 return self.isInterleave(s1, s2[1:], s3[1:])
#         return False


# Now try to convert to DP:

#

class Solution(object):
    def isInterleave(self, s1, s2, s3):


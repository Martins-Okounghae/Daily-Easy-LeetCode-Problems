# Permutation in String

def checkInclusion(s1, s2):

   len1, len2 = len(s1), len(s2)

   if len1 > len2:
       return False

   a = ord('a')

   s1map = [0] * 26
   s2map = [0] * 26

   for i in range(len1):
       s1map[ord(s1[i]) - a] += 1
       s2map[ord(s2[i]) - a] += 1

   for i in range(len2 - len1):
       if s1map == s2map:
           return True
       s2map[ord(s2[i + len1]) - a] += 1
       s2map[ord(s2[i]) - a] -= 1
   return s1map == s2map



result = checkInclusion("ab", "eidbaooo")

print(result)
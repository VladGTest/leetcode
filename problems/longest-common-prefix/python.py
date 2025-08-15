class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if (len(strs) == 0): return ""


        for i in range(len(strs[0])):
            char = strs[0][i]
            for j in range(len(strs)):
                if(i >= len(strs[j]) or strs[j][i] != char):
                    return strs[0][slice(0, i)]
                
            
        

        return strs[0]
        
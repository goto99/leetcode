class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        #helper function
        def isPalindrome(string):
            if len(string) <= 1 or string == string[::-1]:
                return True
            else:
                return False
        # the idea behind is to test s; s[1:]/s[:-1]; s[2:]/s[1:-1]/s[:-2]; s[3:]/s[2:-1]/s[1:-2]/s[:-3];....
        # every step the total length is 1 shorter.
        step = 0
        if isPalindrome(s):
            return s
        else:
            step += 1
            while step < len(s):
 		if isPalindrome(s[step:]):
		    return s[step:])
 		for i in range(1: step):
		    if isPalindrome(s[step-i:-i]):
 			return s[step-i:-i]
                if isPalindrome(s[:-step]):
              	    return s[:-step]
		step += 1
             

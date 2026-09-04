class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        hash = {}
        palindromes = []

        for i, v in enumerate(range(len(s)-2)):
            start, end = i, i + 3
            Substring = s[start:end]

            print(Substring)

            if Substring[::-1] == Substring:
                print ("Palindrome.")
            

            
            # hash[i] = v
            # palindromes.append(hash[i])
  
    
        # print(hash,"\n", palindromes, palindromes[::-1])

s = "aaaaaaa"
Solution().countPalindromicSubsequence(s)

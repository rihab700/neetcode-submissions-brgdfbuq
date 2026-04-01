class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ","").lower()
        new_s = ""
        revesed_s = ""
        for char in s:
            if 97<=ord(char)<=122 or 48 <= ord(char) <= 57  :
                new_s = new_s + char
                revesed_s =  char + revesed_s
        return new_s == revesed_s

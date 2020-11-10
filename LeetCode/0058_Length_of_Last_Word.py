class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        try:
            #split the string by space and get the length of last item in the array
            return len(s.split()[-1])
        except IndexError: #handle empty string
            return 0

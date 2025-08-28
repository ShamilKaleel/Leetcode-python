class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.casefold()
        ascii_text=[ord(ch) for ch in s if ord('a') <= ord(ch) <= ord('z') or ord('0') <=ord(ch) <=ord('9') ]
        # print(ascii_text)
        # ascii_letter=[n for n in ascii_text if ord('a') <= n <= ord('z')]
        # print(ascii_letter)
        # if len(ascii_text)/2 ==1:
        #     return False
        text="".join(chr(n) for n in ascii_text)

        return text == "".join(reversed(text))

        return True
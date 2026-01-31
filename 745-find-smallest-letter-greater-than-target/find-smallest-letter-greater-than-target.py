class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left,right = 0,len(letters)-1
        ans = right + 1

        while left <= right:
            mid = left + (right-left)//2

            if ord(letters[mid]) > ord(target):
                ans = mid
                right = mid -1
            else :
                left = mid + 1
        
        return letters[ans] if ans < len(letters) else letters[0]
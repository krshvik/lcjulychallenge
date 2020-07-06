class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        lend =len(digits)-1
        addi = 1 
        while lend >= 0:
            if digits[lend]  < 9:
                digits[lend] = digits[lend] + addi
                return digits
            else:
                digits[lend] = 0
            lend = lend-1
        return [1] + digits            
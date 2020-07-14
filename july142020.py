class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        if hour == 12:
            hour = 0 
        hour = (hour*5)+(5*(minutes/60))
        val = abs(hour-minutes)
        diff = val*6
        if diff > 180:
            diff = 360-diff
        return diff
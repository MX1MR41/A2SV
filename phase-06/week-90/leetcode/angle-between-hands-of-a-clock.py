class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        if hour == 12:
            hour = 0

        hour_arm = (hour * 5) + ((minutes/60) * 5)
        minute_arm = minutes

        arc = min(
            max(hour_arm, minute_arm) - min(hour_arm, minute_arm),
            min(hour_arm, minute_arm) + 60 - max(hour_arm, minute_arm)
        )


        angle = (arc/60) * 360

        return angle
        

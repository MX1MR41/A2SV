class Solution:
    def minimumTotalDistance(self, robot, factory):
        # sorting + dp
        # use a pick or no-pick approach to choose the best way to fix each robot


        # sort robots and factories 
        robot.sort()
        factory.sort()

        # flatten factory positions according to their capacities
        factory_positions = []
        for f in factory:
            for _ in range(f[1]):
                factory_positions.append(f[0])

        robot_count, factory_count = len(robot), len(factory_positions)
        dp = [[0] * (factory_count + 1) for _ in range(robot_count + 1)]

        # base cases
        for i in range(robot_count):
            dp[i][factory_count] = float("inf")  # no factories left

        # Fill DP table bottom-up starting from the bottom-left towards top-left
        for i in reversed(range(robot_count)):
            for j in reversed(range(factory_count)):
                # Option 1: Assign current robot to current factory
                assign = abs(robot[i] - factory_positions[j]) + dp[i + 1][j + 1]

                # Option 2: Skip current factory for the current robot
                skip = dp[i][j + 1]

                dp[i][j] = min(assign, skip)  # Take the minimum option

        # Minimum distance starting from first robot and factory
        return dp[0][0]  

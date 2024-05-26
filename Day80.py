# 552. Student Attendance Record IIclass Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7

        dp = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(n + 1)]

        dp[0][0][0] = 1

        for i in range(1, n+1):
            for j in range(2):
                for k in range(3):
                   
                    dp[i][j][0] = (dp[i][j][0] + dp[i-1][j][k]) % MOD
                
                    if k < 2:
                        dp[i][j][k+1] = (dp[i][j][k+1] + dp[i-1][j][k]) % MOD
                    
                    if j < 1:
                        dp[i][j+1][0] = (dp[i][j+1][0] + dp[i-1][j][k]) % MOD

        answer = 0
        for j in range(2):
            for k in range(3):
                answer = (answer + dp[n][j][k]) % MOD

        return answer

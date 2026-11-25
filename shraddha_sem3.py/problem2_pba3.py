def climbimg_stairs(n):
  if n<= 1:
    return 1

  dp = [0] * (n+1)

  dp[0] = 1
  dp[1] = 1

  for i in range(2, n+1):
       dp[1] = dp[i-1] + dp[i-2]

  return dp[n]

n =  int(integer("Enter number of stairs: "))

print("Total number of ways:", climbing_stairs(n))

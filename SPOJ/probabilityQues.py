pct = float(input())
pot = float(input())
n = int(input())

carWorkReachOnTime = pot*(1-pct)
carNotWorksReachOnTime =  pct*2/n

reachOnTime = carWorkReachOnTime + carNotWorksReachOnTime
print(round(reachOnTime,6))
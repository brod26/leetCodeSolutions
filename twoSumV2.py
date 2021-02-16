def twosum(s,target):
    low, high = 0, len(s) -1
    while True:
        sum = s[low] + s[high]
        if sum < target: 
            low +=1
        elif sum > target:
            high -=1
        return [low+1, high+1]
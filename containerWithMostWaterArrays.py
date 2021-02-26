# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
# Example 2:

# Input: height = [1,1]
# Output: 1

# Example 3:

# Input: height = [4,3,2,1,4]
# Output: 16

# Example 4:

# Input: height = [1,2,1]
# Output: 2


def maxArea(height) -> int:
    
    dpTable = [[0 for i in range(len(height))] for i in range(len(height))]
    
    for i in range(len(dpTable)):
        for j in range(i,len(dpTable)):
            if j == len(height) and height[-1] < height[i]:
                dpTable[i][j+1] = max(dpTable[i-1][j], dpTable[i][j-1])
            
            else:
                
                dpTable[i][j] = max(
                    height[i]*(j),
                    dpTable[i-1][j],
                    dpTable[i][j-1]
                )
    
    return dpTable[-2][-1]
    

input = [3,9,3,4,7,2,12,6]
print(maxArea(input))
    
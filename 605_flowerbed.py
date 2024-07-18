"""

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
 

Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length

"""

'Solution 1:' 


def canPlaceFlowers(flowerbed, n):
    
    # Add a zero at the beginning and end of the flowerbed to simplify boundary conditions
    flowerbed = [0] + flowerbed + [0]

    # Iterate through the flowerbed from the second element to the second to last element
    for i in range(1, len(flowerbed) - 1):
        
        # Check if the current position and its neighbors are empty
        if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
            
            # Place a flower at the current position
            flowerbed[i] = 1
            
            # Decrease the count of flowers needed
            n -= 1

            # If no more flowers are needed, return True
            if n == 0:
                return True

    # If we exit the loop, return whether we have placed all the needed flowers
    return n <= 0


'Solution: 2'


def canPlaceFlowers(flowerbed, n):
    
    # Length of the flowerbed
    length = len(flowerbed)
    
    # Iterate through the flowerbed
    for i in range(length):
        # Check if the current spot is empty and the neighbors (if any) are also empty
        if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == length-1 or flowerbed[i+1] == 0):
            # Place a flower at the current spot
            flowerbed[i] = 1
            # Decrease the count of flowers needed
            n -= 1
            
            # If no more flowers are needed, return True
            if n == 0:
                return True
                
    # If we exit the loop, return whether we have placed all the needed flowers
    return n <= 0


print(canPlaceFlowers([0,1,0,0,0,1,0],2))


"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.


Input:  
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1


"""

def maxArea(height):
    # Initialize the left pointer at the beginning of the list
    left = 0
    
    # Initialize the right pointer at the end of the list
    right = len(height) - 1
    
    # Initialize the variable to store the maximum water capacity found
    max_capacity = 0
    
    # Loop until the left pointer is less than the right pointer
    while left < right:
        # Calculate the width between the two pointers
        width = right - left
        
        # Determine the shorter line between the two pointers
        min_height = min(height[left], height[right])
        
        # Calculate the water capacity between the two pointers
        water_capacity = width * min_height
        
        # Update the maximum capacity if the current capacity is greater
        max_capacity = max(max_capacity, water_capacity)
        
        # Move the left pointer right if the height at the left pointer is less
        # This is to try to find a taller line that might increase the capacity
        if height[left] < height[right]:
            left += 1
        else:
            # Otherwise, move the right pointer left
            # This is to try to find a taller line from the right end
            right -= 1
    
    # Return the maximum water capacity found
    return max_capacity





print(maxArea([1,8,6,2,5,4,8,3,7]))





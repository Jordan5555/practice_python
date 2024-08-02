"""

There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.

You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

 

Example 1:

Input: gain = [-5,1,5,0,-7]
Output: 1
Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.
Example 2:

Input: gain = [-4,-3,-2,-1,4,3,2]
Output: 0
Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.
 

Constraints:

n == gain.length
1 <= n <= 100
-100 <= gain[i] <= 100

"""


'Solution 1: '


def largestAltitude(gain):

    # Prepend 0 to gain array to start altitude calculation from 0
    gain = [0] + gain
    
    # Calculate maximum altitude reached during the journey
    return max(sum(gain[:x+1]) for x in range(len(gain)))



'Solution 2:'

def largestAltitude(gain):

    # Initialize variables
    # Variable to store the maximum altitude reached
    max_altitude = 0  

    # Variable to keep track of current altitude, starting from sea level (0)
    current_altitude = 0  
    
    # Iterate through each altitude change (gain)
    for change in gain:

        # Update current altitude by adding the current altitude change
        current_altitude += change
        
        # Update max altitude to the maximum of current max altitude or updated current altitude
        max_altitude = max(max_altitude, current_altitude)
    
    # Return the maximum altitude reached during the journey
    return max_altitude




print(largestAltitude([-4,-3,-2,-1,4,3,2]))
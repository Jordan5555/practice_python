"""


You are given an integer money denoting the amount of money (in dollars) that you have and another integer children denoting the number of children that you must distribute the money to.

You have to distribute the money according to the following rules:

All money must be distributed.
Everyone must receive at least 1 dollar.
Nobody receives 4 dollars.
Return the maximum number of children who may receive exactly 8 dollars if you distribute the money according to the aforementioned rules. If there is no way to distribute the money, return -1.

 

Example 1:

Input: money = 20, children = 3
Output: 1
Explanation: 
The maximum number of children with 8 dollars will be 1. One of the ways to distribute the money is:
- 8 dollars to the first child.
- 9 dollars to the second child. 
- 3 dollars to the third child.
It can be proven that no distribution exists such that number of children getting 8 dollars is greater than 1.
Example 2:

Input: money = 16, children = 2
Output: 2
Explanation: Each child can be given 8 dollars.
 
 
 
 """


def dist_money(self, money: int, children: int) -> int:
    # If there is less money than children, distribution isn't possible.
    if money < children:
        return -1
    
    # If money exceeds 8 times the number of children, each child can receive
    # at least one coin and the solution approaches the number of children minus 1.
    # This is because we can distribute 7 coins without forming an octagon.
    if money > 8 * children:
        return children - 1
    
    # If the amount of money is exactly 4 less than 8 times the number of children,
    # we face a specific case where we cannot form a complete last octagon and
    # therefore, must subtract an additional child from the normally expected count.
    if money == 8 * children - 4:
        return children - 2
    
    # In cases where the constraints above aren't met, the number of children that
    # need to be skipped (to avoid creating octagons) can be calculated by dividing
    # the excess money over a 1-to-1 distribution by 7. This ensures that the distribution
    # does not allow for an octagon's worth of coins (8) to any child.
    return (money - children) // 7
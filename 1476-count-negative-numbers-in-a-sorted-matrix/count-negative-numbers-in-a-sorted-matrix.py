class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # finding the tot values which are neg in the grid
        # initial approach - iterate over all the grid elements and count the negatives
        # Tc = O(mn) 
        # Sc = O(1)

        # optimizing possible
        # [---nnnn]
        # [-n-n---]
        # [-n-n---]
        # [-n-n---]

        #Thoughts
        # Using Binary Search
        # Tc = O(mlog(n))

        # starting iteration from Top right with rules:
        # moving down until neg is found
        # moving left if neg is found until a pos is seen
        # counting the values in iteration

        rows, cols = len(grid), len(grid[0])
        cur_row, cur_col = 0, cols-1
        prev_col = cols-1
        negs = 0
        while cur_row < rows and cur_col >= 0:
            while cur_col >= 0 and grid[cur_row][cur_col] < 0:
                cur_col -= 1
            negs += (prev_col - cur_col)*(rows - cur_row)
            prev_col = cur_col
            cur_row += 1
        return negs














class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        # finding whether we can reach the top of pyramid with given base and allowed sequences
        # Finding all the possible next levels with given base
        # Trying all the possible next levels as bases to find they can form a pyramid
        # If any of them returns True will return True

        pool = defaultdict(list)
        for p in allowed:
            pool[p[:2]].append(p[2])

        @lru_cache(None)
        def dfs(current_row):
            if len(current_row) == 1:
                return True
            
            # Inner DFS to build the next row character by character
            # This allows us to "fail fast" inside the row construction
            def build_next(index, partial_next_row):
                # If we built the full next row, recurse up
                if index == len(current_row) - 1:
                    return dfs(partial_next_row)
                
                # Try all allowed tops for the current pair
                key = current_row[index : index+2]
                for valid_top in pool[key]:
                    # Standard backtracking:
                    # Append char -> Recurse -> (Implicitly backtrack if loop continues)
                    if build_next(index + 1, partial_next_row + valid_top):
                        return True
                return False

            return build_next(0, "")

        return dfs(bottom)
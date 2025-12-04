class Solution:
    def countCollisions(self, directions: str) -> int:
        collisions = directions.lstrip('L').rstrip('R')
        return len(collisions) - collisions.count("S") 

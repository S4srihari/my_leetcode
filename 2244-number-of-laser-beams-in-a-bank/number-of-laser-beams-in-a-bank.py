class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prevLasers = 0
        beams = 0
        for row in bank:
            lasers = row.count('1')
            if lasers:
                beams += prevLasers*lasers
                prevLasers = lasers
        return beams
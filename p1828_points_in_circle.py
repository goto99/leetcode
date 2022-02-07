#!/usr/bin/env python
# File: p1828_points_in_circle.py
# Difficulty: easy

class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
	# helper function 
        def inside(c, p):
            return (c[0] - p[0]) ** 2 + (c[1] - p[1]) ** 2 <= c[2] ** 2

        answer = []
        for c in queries:
            count = 0
            for p in points:
                if inside(c, p):
                    count += 1
            answer.append(count)
        
        return answer

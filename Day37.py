# 85. Maximal Rectangle

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0

        for row in range(rows):
            for col in range(cols):
                heights[col] = heights[col] + 1 if matrix[row][col] == '1' else 0

            max_area = max(max_area, self.largestRectangleArea(heights))

        return max_area

    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0
        heights.append(0)

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)

        return max_area

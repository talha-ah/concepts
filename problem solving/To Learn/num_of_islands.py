class Solution(object):
    def num_of_islands(self, grid):

        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    count += 1
                    self.call_bfs(grid, i, j)

        return count

    def call_bfs(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == "0":
            return

        grid[i][j] = "0"
        self.call_bfs(grid, i + 1, j)  # top
        self.call_bfs(grid, i - 1, j)  # bottom
        self.call_bfs(grid, i, j - 1)  # left
        self.call_bfs(grid, i, j + 1)  # right


input = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]


print(Solution().num_of_islands(input))
# expected = 1

input = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]

print(Solution().num_of_islands(input))
# expected = 3

import random
import sys


# mazeCreator.py
# spring 2024
# prof. lehmaan
#
# creates a maze saving to file
#
#  ..X...
#  ...X..B
#  .......
#  ...XX..

# Chat GPT 4 prompt 2.2.2024
# Using Python code,  create a random maze generator.
# The program random mazes that are R rows by C columns.
# Use X to denote a wall.  Use space to denote an open path.
# Display the maze to the screen.
# Asked it to add code to save to file.
# Updated spadce to "." to assist reading file.
# note: had to import random, otherwise code worked first time!


class Maze:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.maze = [['X' for _ in range(cols * 2 - 1)] for _ in range(rows * 2 - 1)]

    def generate_maze(self):
        def dfs(x, y):
            directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]
            random.shuffle(directions)

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.rows * 2 - 1 and 0 <= ny < self.cols * 2 - 1 and self.maze[nx][ny] == 'X':
                    self.maze[nx][ny] = '.'
                    self.maze[x + dx // 2][y + dy // 2] = '.'
                    dfs(nx, ny)

        # Start DFS from the upper-left corner
        self.maze[0][0] = '.'
        dfs(0, 0)

    def display_maze(self):
        for row in self.maze:
            print(''.join(row))

    def save_maze_to_file(self, filename="maze_1.txt"):
        with open(filename, 'w') as file:
            for row in self.maze:
                file.write(''.join(row) + '\n')
        print(f"Maze saved to {filename}")

# Example usage

# Check the current recursion limit
current_limit = sys.getrecursionlimit()
print("Current recursion limit:", current_limit)

# Set a new recursion limit
new_limit = 2000  # You can adjust this value as needed
sys.setrecursionlimit(new_limit)

# Verify the new recursion limit
print("New recursion limit:", sys.getrecursionlimit())

maze = Maze(3, 5)
maze.generate_maze()
maze.display_maze()
maze.save_maze_to_file()  # This will save the maze to maze.txt



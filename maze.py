import random

class Maze_class:
    def __init__(self):
        self.maze = {}

    def create_walls(self):
            self.view_maze
            for horizontal in range(10):
                for vertical in range(10):
                    self.maze[(horizontal, vertical)] = "🧱"
            print(self.maze)

 
    def create_paths(self):
        entry = self.maze[(horizontal, vertical)]
                    

instance = Maze_class()

instance.create_walls()

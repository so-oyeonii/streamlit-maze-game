"""
Maze generation and game logic for the maze game.
Uses recursive backtracking algorithm to generate random mazes.
"""

import random
import numpy as np


class Maze:
    """Class to generate and manage maze game logic."""
    
    def __init__(self, width=15, height=15):
        """
        Initialize a new maze.
        
        Args:
            width: Width of the maze (odd number recommended)
            height: Height of the maze (odd number recommended)
        """
        self.width = width if width % 2 == 1 else width + 1
        self.height = height if height % 2 == 1 else height + 1
        self.maze = np.ones((self.height, self.width), dtype=int)
        self.player_pos = [1, 1]
        self.goal_pos = [self.height - 2, self.width - 2]
        self.generate_maze()
        
    def generate_maze(self):
        """Generate a maze using recursive backtracking algorithm."""
        # Start from position (1, 1)
        start_x, start_y = 1, 1
        self.maze[start_y][start_x] = 0
        
        # Stack for backtracking
        stack = [(start_x, start_y)]
        
        while stack:
            current_x, current_y = stack[-1]
            
            # Find unvisited neighbors
            neighbors = []
            
            # Check all four directions (up, right, down, left)
            directions = [
                (0, -2),  # up
                (2, 0),   # right
                (0, 2),   # down
                (-2, 0)   # left
            ]
            
            for dx, dy in directions:
                nx, ny = current_x + dx, current_y + dy
                
                # Check if the neighbor is within bounds and unvisited
                if (0 < nx < self.width - 1 and 
                    0 < ny < self.height - 1 and 
                    self.maze[ny][nx] == 1):
                    neighbors.append((nx, ny, dx, dy))
            
            if neighbors:
                # Choose a random unvisited neighbor
                nx, ny, dx, dy = random.choice(neighbors)
                
                # Remove wall between current cell and chosen neighbor
                wall_x = current_x + dx // 2
                wall_y = current_y + dy // 2
                self.maze[wall_y][wall_x] = 0
                self.maze[ny][nx] = 0
                
                # Add neighbor to stack
                stack.append((nx, ny))
            else:
                # Backtrack if no unvisited neighbors
                stack.pop()
        
        # Ensure start and goal positions are open
        self.maze[1][1] = 0
        self.maze[self.height - 2][self.width - 2] = 0
    
    def move_player(self, direction):
        """
        Move the player in the specified direction.
        
        Args:
            direction: One of 'up', 'down', 'left', 'right'
            
        Returns:
            bool: True if move was successful, False otherwise
        """
        new_pos = self.player_pos.copy()
        
        if direction == 'up':
            new_pos[0] -= 1
        elif direction == 'down':
            new_pos[0] += 1
        elif direction == 'left':
            new_pos[1] -= 1
        elif direction == 'right':
            new_pos[1] += 1
        else:
            return False
        
        # Check if the new position is valid (within bounds and not a wall)
        if (0 <= new_pos[0] < self.height and 
            0 <= new_pos[1] < self.width and 
            self.maze[new_pos[0]][new_pos[1]] == 0):
            self.player_pos = new_pos
            return True
        
        return False
    
    def check_win(self):
        """
        Check if the player has reached the goal.
        
        Returns:
            bool: True if player is at goal position
        """
        return (self.player_pos[0] == self.goal_pos[0] and 
                self.player_pos[1] == self.goal_pos[1])
    
    def reset(self):
        """Reset the player position to the start."""
        self.player_pos = [1, 1]
    
    def get_display_maze(self):
        """
        Get a copy of the maze with player and goal positions marked.
        
        Returns:
            numpy.ndarray: Maze with special markers
                0: path
                1: wall
                2: player
                3: goal
        """
        display = self.maze.copy()
        display[self.goal_pos[0]][self.goal_pos[1]] = 3
        display[self.player_pos[0]][self.player_pos[1]] = 2
        return display

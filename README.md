# 🎮 Streamlit Maze Game

An interactive maze game built with Streamlit. Navigate through randomly generated mazes to reach the goal!

## 📋 Features

- 🎲 Randomly generated mazes using recursive backtracking algorithm
- 🎮 Interactive controls for player movement
- 📊 Move counter to track your progress
- 🔄 Multiple maze sizes (Small, Medium, Large)
- 🎯 Clear visual representation with emojis
- 🏆 Win condition detection

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/so-oyeonii/streamlit-maze-game.git
cd streamlit-maze-game
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

## 🎯 How to Run

Run the Streamlit app:
```bash
streamlit run app.py
```

The app will open in your default web browser at `http://localhost:8501`.

## 🕹️ How to Play

1. **Start Position**: You begin at the green circle (🟢) in the top-left area of the maze
2. **Goal**: Navigate to reach the target (🎯) in the bottom-right area
3. **Movement**: Use the arrow buttons below the maze to move in four directions
4. **Obstacles**: Black squares (⬛) are walls - you cannot pass through them
5. **Path**: White squares (⬜) are walkable paths
6. **Win**: Reach the goal in as few moves as possible!

## 🎨 Game Elements

- 🟢 **Green Circle**: Your current position
- 🎯 **Target**: The goal you need to reach
- ⬛ **Black Square**: Walls (impassable)
- ⬜ **White Square**: Path (walkable)

## ⚙️ Features in the Sidebar

- **Maze Size**: Choose between Small (11x11), Medium (15x15), or Large (21x21)
- **New Maze**: Generate a completely new random maze
- **Reset Position**: Reset your position to the start without generating a new maze
- **Statistics**: Track the number of moves you've made

## 📁 Project Structure

```
maze-game/
├── app.py                 # Main Streamlit app
├── maze.py               # Maze generation and game logic
├── requirements.txt      # Required packages
├── README.md            # Project description
└── .gitignore           # Git ignore file
```

## 🛠️ Technologies Used

- **Streamlit**: Web application framework
- **NumPy**: Numerical computations for maze generation
- **Python**: Programming language

## 📝 Code Overview

### maze.py
Contains the `Maze` class with the following key methods:
- `generate_maze()`: Creates a random maze using recursive backtracking
- `move_player(direction)`: Handles player movement
- `check_win()`: Checks if the player reached the goal
- `get_display_maze()`: Returns the maze state for display

### app.py
The main Streamlit application that:
- Manages game state using Streamlit session state
- Provides an interactive UI for the game
- Displays the maze and handles user input
- Shows game statistics and win condition

## 🤝 Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Created by so-oyeonii
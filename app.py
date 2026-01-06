"""
Main Streamlit application for the maze game.
"""

import streamlit as st
from maze import Maze


def display_maze(maze_obj):
    """
    Display the maze in the Streamlit app using colored cells.
    
    Args:
        maze_obj: Maze object to display
    """
    display = maze_obj.get_display_maze()
    
    # Create HTML representation of the maze
    html = '<div style="font-family: monospace; line-height: 1.2;">'
    
    for row in display:
        html += '<div style="display: flex;">'
        for cell in row:
            if cell == 1:  # Wall
                color = '#333333'
                symbol = '⬛'
            elif cell == 2:  # Player
                color = '#4CAF50'
                symbol = '🟢'
            elif cell == 3:  # Goal
                color = '#FFD700'
                symbol = '🎯'
            else:  # Path
                color = '#FFFFFF'
                symbol = '⬜'
            
            html += f'<span style="color: {color}; font-size: 20px;">{symbol}</span>'
        html += '</div>'
    
    html += '</div>'
    
    st.markdown(html, unsafe_allow_html=True)


def main():
    """Main application function."""
    st.set_page_config(
        page_title="Maze Game",
        page_icon="🎮",
        layout="centered"
    )
    
    st.title("🎮 Maze Game")
    st.markdown("Navigate through the maze to reach the goal!")
    
    # Initialize session state
    if 'maze' not in st.session_state:
        st.session_state.maze = Maze(width=15, height=15)
        st.session_state.moves = 0
        st.session_state.game_won = False
    
    # Sidebar controls
    with st.sidebar:
        st.header("⚙️ Settings")
        
        # Maze size selection
        size = st.selectbox(
            "Maze Size",
            options=[("Small (11x11)", 11), ("Medium (15x15)", 15), ("Large (21x21)", 21)],
            format_func=lambda x: x[0],
            index=1
        )
        
        if st.button("🔄 New Maze"):
            st.session_state.maze = Maze(width=size[1], height=size[1])
            st.session_state.moves = 0
            st.session_state.game_won = False
            st.rerun()
        
        if st.button("↩️ Reset Position"):
            st.session_state.maze.reset()
            st.session_state.moves = 0
            st.session_state.game_won = False
            st.rerun()
        
        st.markdown("---")
        st.header("📊 Statistics")
        st.metric("Moves", st.session_state.moves)
        
        st.markdown("---")
        st.header("🎮 Controls")
        st.markdown("""
        - Use the arrow buttons below the maze to move
        - 🟢 Green: Your position
        - 🎯 Target: Goal
        - ⬛ Black: Walls
        - ⬜ White: Path
        """)
    
    # Check for win condition
    if st.session_state.maze.check_win() and not st.session_state.game_won:
        st.session_state.game_won = True
    
    # Display game status
    if st.session_state.game_won:
        st.success(f"🎉 Congratulations! You won in {st.session_state.moves} moves!")
    else:
        st.info("Use the buttons below to navigate through the maze")
    
    # Display the maze
    display_maze(st.session_state.maze)
    
    # Movement controls
    st.markdown("### Move:")
    
    col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])
    
    with col1:
        if st.button("⬅️ Left", use_container_width=True):
            if st.session_state.maze.move_player('left'):
                st.session_state.moves += 1
            st.rerun()
    
    with col2:
        if st.button("⬆️ Up", use_container_width=True):
            if st.session_state.maze.move_player('up'):
                st.session_state.moves += 1
            st.rerun()
    
    with col3:
        if st.button("⬇️ Down", use_container_width=True):
            if st.session_state.maze.move_player('down'):
                st.session_state.moves += 1
            st.rerun()
    
    with col4:
        if st.button("➡️ Right", use_container_width=True):
            if st.session_state.maze.move_player('right'):
                st.session_state.moves += 1
            st.rerun()
    
    # Additional info
    st.markdown("---")
    st.markdown("""
    ### How to Play:
    1. Start at the green position (🟢) in the top-left area
    2. Navigate through the white paths (⬜)
    3. Reach the goal (🎯) in the bottom-right area
    4. Try to complete the maze in as few moves as possible!
    """)


if __name__ == "__main__":
    main()

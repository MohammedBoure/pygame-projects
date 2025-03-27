# Pygame Circle Path & Editor

A simple Pygame application demonstrating path visualization between two circles and featuring a basic interactive level editor to add or remove obstacle blocks.

## Features

*   **Circle Movement:** Move designated red and blue circles around the grid.
*   **Path Visualization:** See a preview line when dragging a circle, indicating the potential path.
    *   **Red Line:** The path to the target location is clear.
    *   **Blue Line:** The path to the target location is blocked by an obstacle.
*   **Drag-and-Drop:** Circles move to the target location upon releasing the mouse button, but only if the visualized path was clear (red).
*   **Interactive Level Editor:** Modify the game environment by adding or removing wall obstacles.
    *   Select grid cells using the right mouse button.
    *   Cycle through different obstacle types (e.g., horizontal/vertical segments) with subsequent right-clicks on the *same* cell.
    *   Add obstacles to the selected cell using the 'd' key.
    *   Remove obstacles from the selected cell using the 's' key.

## Requirements

*   Python 3.x
*   Pygame library

## Installation

1.  **Clone or Download:** Get the project files (`main.py`, `game.py`, `function.py`, `constants.py`).
2.  **Navigate:** Open a terminal or command prompt and navigate to the directory containing the downloaded files.
3.  **Install Pygame:** If you don't have Pygame installed, run:
    ```bash
    pip install pygame
    ```

## How to Run

Execute the main script from your terminal:

```bash
python main.py
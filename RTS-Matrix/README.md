
# Infinite Grid Strategy Game

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Pygame](https://img.shields.io/badge/Pygame-2.x-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## Overview
A simple strategy game built with **Pygame** in Python, featuring an infinite grid where players can place colored units, move the grid, and adjust cell sizes using mouse and keyboard inputs. This project serves as a foundation for a customizable strategy game that can be expanded with additional features.

### Files
- **`main.py`**: Core game logic (grid rendering, unit management, input handling).
- **`function.py`**: Helper functions (`draw_text` for text rendering, `get_mouse_direction` for mouse movement detection).

## Features
- **Dynamic Grid**: Resizeable grid cells via mouse wheel (zoom in/out).
- **Unit Placement**: Left-click to add blue units to the grid.
- **Grid Navigation**: Move the grid using arrow keys (left, right, up, down).
- **Info Display**: Real-time display of `Offset X`, `Offset Y`, and `Grid Size`.
- **Visual Units**: Units rendered as colored squares (blue and red currently).

## Benefits
- **Beginner-Friendly**: Clean and simple code, ideal for learning Pygame basics.
- **Extensible**: Easy to build upon with combat, AI, or multiplayer features.
- **Interactive**: Smooth mouse and keyboard controls enhance usability.
- **Infinite Space**: Offset-based grid allows exploration of a virtually unlimited area.

## Installation
1. Ensure you have Python 3.x installed.
2. Install Pygame:
   ```bash
   pip install pygame
   ```
3. Clone this repository:
   ```bash
   git clone https://github.com/your-username/infinite-grid-strategy-game.git
   cd infinite-grid-strategy-game
   ```
4. Run the game:
   ```bash
   python main.py
   ```

### Controls
- **Left Click**: Place a blue unit.
- **Mouse Wheel Up/Down**: Zoom in/out.
- **Arrow Keys**: Move grid (left, right, up, down).
- **Window Close**: Exit the game.


## Potential Enhancements
1. **Gameplay**:
   - Combat system (e.g., red vs. blue units).
   - Unit stats (health, attack power).
2. **Graphics**:
   - Replace squares with sprites or icons.
   - Add animations for actions like placement or movement.
3. **AI**:
   - Automated red unit behavior (movement, attacking).
4. **Multiplayer**:
   - Local or networked multiplayer support.
5. **UI**:
   - Main menu, in-game HUD, or stats panel.
6. **Persistence**:
   - Save/load game state (unit positions, grid settings).


## Notes
- The `get_mouse_direction` function could be refined for more precise mouse movement handling.
- Performance optimization may be needed for large numbers of units or grid sizes.

## License
This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute it as you see fit.



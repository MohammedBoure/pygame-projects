# Pygame Rotating 3D Sphere

A visually enhanced Pygame application that renders a sphere composed of points and allows interactive rotation in 3D space using the mouse.

## Features

*   **3D Sphere Representation:** Generates points distributed across the surface of a sphere using spherical coordinates (latitude and longitude).
*   **Smooth Rotation:**
    *   **Automatic:** The sphere rotates slowly and continuously around the Y-axis.
    *   **Interactive:** Click and drag the left mouse button to rotate the sphere freely around the X and Y axes.
*   **Depth Cueing:** Points appear larger and brighter the closer they are to the viewer (based on their Z-coordinate after rotation), providing a sense of depth.
*   **Correct Occlusion:** Uses a simple Painter's Algorithm (sorting points by depth before drawing) to ensure points closer to the viewer correctly overlap points further away.
*   **Clean Rendering:** Uses `pygame.draw.circle` for smoother points and `pygame.time.Clock` for consistent frame rate and animation.

## Requirements

*   Python 3.x
*   Pygame library

## Installation

1.  **Clone or Download:** Get the Python script file (e.g., `sphere_rotation.py`).
2.  **Navigate:** Open a terminal or command prompt and navigate to the directory containing the file.
3.  **Install Pygame:** If you don't have Pygame installed, run:
    ```bash
    pip install pygame
    ```
    *(or `pip3 install pygame`)*

## How to Run

Execute the script from your terminal:

```bash
python main.py
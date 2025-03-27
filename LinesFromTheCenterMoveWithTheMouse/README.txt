# Raycasting with Moving Obstacles

## Overview
This is a simple raycasting visualization implemented using Pygame. The program simulates rays originating from a moving marker, which interact with obstacles and screen boundaries. The obstacles move dynamically and cause the rays to be blocked upon intersection.

## Features
- **Real-time Raycasting:** Casts rays in multiple directions from a central point.
- **Dynamic Obstacles:** Rectangular obstacles move and bounce off screen edges.
- **Mouse-Controlled Marker:** The source of the rays follows the mouse position.
- **Efficient Intersection Detection:** Optimized calculations to find the closest intersection.
- **Smooth Animation:** Maintains a steady 60 FPS for fluid motion.

## Requirements
- Python 3.x
- Pygame library (`pip install pygame`)

## Installation
1. Clone or download this repository.
2. Install dependencies using:
   ```sh
   pip install pygame
   ```
3. Run the script:
   ```sh
   python main.py
   ```

## How to Use
- Move the mouse around to change the ray source position.
- Observe how the rays interact with moving obstacles and walls.

## Customization
- Adjust `NUM_RADIAL_LINES` to increase or decrease the number of rays.
- Modify `num_obstacles` to change the number of obstacles.
- Change the obstacle speed by tweaking the velocity range in the initialization section.

## License
This project is open-source and available under the MIT License.


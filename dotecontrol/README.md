# Multiplayer Grid Game

## Overview
This is a multiplayer grid-based game built using **Pygame**. The game allows two players to interact in a shared grid environment, moving their respective squares while communicating through a network connection.

## Game Description
The game is a **two-player network-based game** that operates on a grid system. Each player controls a square and moves it according to predefined rules while maintaining synchronization through a network connection.

### Gameplay Mechanics
- The game board consists of a **grid of squares**.
- Each player starts with a square positioned at a specific location.
- Players **select their square by right-clicking**.
- They **move their selected square by left-clicking** on a new position.
- Movement updates are **instantly synchronized over the network** for both players.

### Network Modes
- **Server Mode**: Acts as a central hub to manage game updates and synchronize movements between players.
- **Client Mode**: Connects to the server to receive updates and send movement actions.

## Features
- Multiplayer support via **server-client architecture**.
- Grid-based movement and interaction.
- Player positions are synchronized over the network.
- Simple and clean UI using Pygame.

## Requirements
Make sure you have the following installed:
- Python 3.x
- Pygame (`pip install pygame`)

## Installation & Setup
1. Downlaod Packaged-Project.zip file
   ```
2. Install dependencies:
   ```bash
   pip install pygame
   ```
3. Run the game:
     ```bash
     python main.py 
     ```


## How to Play
- **Right-click** to select a square.
- **Left-click** to move the selected square.
- The game synchronizes movement between two players via the network.

## Networking
- The game supports both **server** and **client** modes.
- The server listens for connections and updates the game state.
- The client connects to the server and synchronizes movements.

## File Structure
```
multiplayer-grid-game/
│── main.py                 # Main game loop
│── game.py                 # Game logic and rendering
│── server.py               # Server and client networking
│── constants.py            # Game constants
│── function.py             # Utility functions
│── README.md               # Documentation
```

## License
This project is open-source and available under the **MIT License**.

---
Feel free to improve and expand the game! 🚀


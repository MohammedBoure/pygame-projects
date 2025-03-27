import pygame

# Assuming your refactored Game class is in 'game.py'
from game import Game 
# Assuming your constants (WHITE, dimensions, FPS) are in 'constants.py'
from constants import WHITE, SCREEN_WIDTH, SCREEN_HEIGHT, FPS 

# --- Initialization ---
pygame.init()

# Create the screen (display surface)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Line Puzzle Game") # Optional: Set a window title

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# --- Create Game Instance ---
# Pass the screen surface to the Game object's constructor
game = Game(screen) 

# --- Main Game Loop ---
running = True
while running:
    # --- Event Handling ---
    # Process all events in the queue
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False # Exit the loop if the window is closed
        
        # Pass the event to the game object for handling
        game.handle_event(event) 
        
    # --- Game Logic Update (if any needed per frame) ---
    # game.update() # If you had separate update logic, call it here

    # --- Drawing ---
    # 1. Clear the screen by filling it with the background color
    #    Do this *before* drawing anything else for the current frame.
    screen.fill(WHITE) 

    # 2. Tell the game object to draw all its elements
    #    The refactored Game class has a draw() method for this.
    game.draw() 

    # 3. Update the full display surface to show everything drawn
    pygame.display.flip() 

    # --- Frame Rate Control ---
    # Wait a specified amount of time to maintain the target FPS
    clock.tick(FPS) 

# --- Cleanup ---
# Uninitialize Pygame modules when the loop ends
pygame.quit() 
# It's good practice to ensure the program exits cleanly, 
# although sometimes sys.exit() is needed depending on the environment.
# import sys 
# sys.exit() 
import pygame
from random import randint
from math import hypot # Using hypot for distance calculation

# Assuming these are imported correctly from your 'function' module
from function import array, dearray, array_circle, is_line_intersect_square
# Assuming these are imported correctly from your 'constants' module
from constants import BLACK, WHITE, RED, BLUE # Corrected WHITH to WHITE

# --- Constants ---
GRID_WIDTH = 21
GRID_HEIGHT = 16
# Estimate cell size based on typical screen/grid ratios or function definitions
# If array() defines size, these might not be strictly needed everywhere
CELL_WIDTH = 40 # Example: 800 / (GRID_WIDTH + some padding?)
CELL_HEIGHT = 40 # Example: 600 / (GRID_HEIGHT + some padding?)
CIRCLE_RADIUS = 7
HIGHLIGHT_BORDER = 2 # Thickness for edit selection highlight

# Edit Mode States
EDIT_STATE_IDLE = 0
EDIT_STATE_SELECTED = 1

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.obstacles = [] # Unified list for all wall/obstacle Rects

        # --- Circle State ---
        self.circle1_pos_grid = (10, 1) # Store grid position
        self.circle2_pos_grid = (10, 15) # Store grid position
        self.circle1_center = array_circle(self.circle1_pos_grid) # Screen coords
        self.circle2_center = array_circle(self.circle2_pos_grid) # Screen coords

        # --- Interaction State ---
        self.dragging_circle = None # None, 1, or 2
        self.mouse_pos = (0, 0)
        self.is_mouse_button_down = False # Track left mouse button state

        # --- Edit Mode State ---
        self.edit_mode_state = EDIT_STATE_IDLE
        self.edit_selection_pos = None # Grid coordinates (x, y)
        self.edit_selection_type = None # Type of block (1 or 2) to add/remove

        self.create_initial_layout()

    def create_initial_layout(self):
        """Initializes the game layout with obstacles and boundaries."""
        self.obstacles.clear() # Ensure list is empty before creation

        # 1. Random internal obstacles
        for i in range(GRID_WIDTH): # Use constants
            for j in range(1, GRID_HEIGHT - 1): # Avoid placing on boundary rows initially
                # Ensure random blocks are not placed on specific start/end zones
                grid_pos = (i, j)
                start_zone_grid = (0, 7)
                end_zone_grid = (20, 7)

                if grid_pos != start_zone_grid and grid_pos != end_zone_grid:
                    # Generate type 1 or 2 randomly
                    block_type = randint(1, 2)
                    obstacle_rect = array(grid_pos, block_type)
                    if obstacle_rect: # Check if array() returned a valid Rect
                        self.obstacles.append(obstacle_rect)

        # 2. Boundary obstacles
        for i in range(GRID_WIDTH + 1): # Cover full width/height
            # Top boundary (type 1 = horizontal?)
            rect_top = array((i, 0), 1)
            if rect_top: self.obstacles.append(rect_top)
            # Bottom boundary (type 1 = horizontal?)
            rect_bottom = array((i, GRID_HEIGHT - 1), 1)
            if rect_bottom: self.obstacles.append(rect_bottom)

        for j in range(GRID_HEIGHT): # Cover full height
             # Left boundary (type 2 = vertical?)
             rect_left = array((0, j), 2)
             if rect_left: self.obstacles.append(rect_left)
             # Right boundary (type 2 = vertical?)
             rect_right = array((GRID_WIDTH, j), 2) # Use GRID_WIDTH for right edge
             if rect_right: self.obstacles.append(rect_right)

        # Ensure specific start/end zones are clear (remove any obstacles there)
        # Note: This assumes array() can represent these zones. Adjust if needed.
        start_rect = array((0, 7), 2) # Example type
        end_rect = array((20, 7), 2) # Example type
        self.obstacles = [obs for obs in self.obstacles if obs != start_rect and obs != end_rect]

    def handle_event(self, event):
        """Handles user input events."""
        self.mouse_pos = pygame.mouse.get_pos() # Update mouse position continuously

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # Left Click
                self.handle_left_click_down()
                self.is_mouse_button_down = True
            elif event.button == 3: # Right Click
                self.handle_right_click()

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1: # Left Click Release
                self.handle_left_click_up()
                self.is_mouse_button_down = False

        elif event.type == pygame.MOUSEMOTION:
             # Motion only relevant if dragging
             pass # self.mouse_pos is updated above

        elif event.type == pygame.KEYDOWN:
            self.handle_key_press(event)

    def handle_left_click_down(self):
        """Handles the start of a left-click (potential drag)."""
        # Check distance to circle centers
        dist1 = hypot(self.mouse_pos[0] - self.circle1_center[0], self.mouse_pos[1] - self.circle1_center[1])
        dist2 = hypot(self.mouse_pos[0] - self.circle2_center[0], self.mouse_pos[1] - self.circle2_center[1])

        click_threshold = CIRCLE_RADIUS * 1.5 # Make clicking slightly easier

        if dist1 < click_threshold:
            self.dragging_circle = 1
        elif dist2 < click_threshold:
            self.dragging_circle = 2
        else:
            self.dragging_circle = None

    def handle_left_click_up(self):
        """Handles the end of a left-click (completing a drag)."""
        if self.dragging_circle is not None:
            can_draw_line, target_center_pos, target_grid_pos = self.check_line_path()

            if can_draw_line:
                # Move the selected circle
                if self.dragging_circle == 1:
                    self.circle1_pos_grid = target_grid_pos
                    self.circle1_center = target_center_pos
                elif self.dragging_circle == 2:
                    self.circle2_pos_grid = target_grid_pos
                    self.circle2_center = target_center_pos

        # Reset dragging state
        self.dragging_circle = None

    def handle_right_click(self):
        """Handles right-clicks for map editing mode."""
        clicked_grid_pos = dearray(self.mouse_pos)
        if not clicked_grid_pos: return # Clicked outside grid?

        if self.edit_mode_state == EDIT_STATE_IDLE:
            # Enter selection mode
            self.edit_mode_state = EDIT_STATE_SELECTED
            self.edit_selection_pos = clicked_grid_pos
            self.edit_selection_type = 1 # Default to type 1 first
        elif self.edit_mode_state == EDIT_STATE_SELECTED:
            if clicked_grid_pos == self.edit_selection_pos:
                # Cycle through types on the same block
                if self.edit_selection_type == 1:
                    self.edit_selection_type = 2
                elif self.edit_selection_type == 2:
                    # Deselect
                    self.edit_selection_pos = None
                    self.edit_selection_type = None
                    self.edit_mode_state = EDIT_STATE_IDLE
            else:
                # Selected a different block
                self.edit_selection_pos = clicked_grid_pos
                self.edit_selection_type = 1 # Start with type 1 again

    def handle_key_press(self, event):
        """Handles key presses for adding/removing obstacles."""
        if self.edit_mode_state == EDIT_STATE_SELECTED and self.edit_selection_pos is not None and self.edit_selection_type is not None:
            target_rect = array(self.edit_selection_pos, self.edit_selection_type)
            if not target_rect: return # Invalid position/type

            if event.key == pygame.K_d: # 'd' to Add/Draw
                # Add if not already present
                if target_rect not in self.obstacles:
                    self.obstacles.append(target_rect)
            elif event.key == pygame.K_s: # 's' to Subtract/Remove
                 # Remove if present
                if target_rect in self.obstacles:
                    self.obstacles.remove(target_rect)
                # Alternative: Use list comprehension for safer removal
                # self.obstacles = [obs for obs in self.obstacles if obs != target_rect]

    def check_line_path(self):
        """
        Checks if a line from the selected circle to the current mouse position
        intersects any obstacles. Returns validity, target center, and target grid pos.
        """
        if self.dragging_circle is None:
            return False, None, None

        # Determine start position
        start_pos = self.circle1_center if self.dragging_circle == 1 else self.circle2_center

        # Determine potential end position (center of the grid cell under the mouse)
        target_grid_pos = dearray(self.mouse_pos)
        if not target_grid_pos: # Mouse is outside grid
             return False, None, None

        # Prevent moving onto the other circle's spot
        other_circle_pos = self.circle2_pos_grid if self.dragging_circle == 1 else self.circle1_pos_grid
        if target_grid_pos == other_circle_pos:
            return False, None, None

        target_center_pos = array_circle(target_grid_pos)
        if not target_center_pos: # Should not happen if dearray worked
            return False, None, None

        # Check for intersections
        s1_x, s1_y = start_pos
        s2_x, s2_y = target_center_pos
        can_draw_line = True
        for obstacle in self.obstacles:
            if is_line_intersect_square(s1_x, s1_y, s2_x, s2_y, obstacle):
                can_draw_line = False
                break

        return can_draw_line, target_center_pos, target_grid_pos

    def draw(self):
        """Draws all game elements onto the screen."""
        # 1. Background
        self.screen.fill(WHITE)

        # 2. Obstacles
        for obstacle in self.obstacles:
            pygame.draw.rect(self.screen, BLACK, obstacle)

        # 3. Special Zones / Overlays (if any, like start/end highlights)
        # Example: Draw white rectangles for start/end zones explicitly if needed
        start_zone_rect = array((0, 7), 2) # Make sure type matches how they are cleared
        end_zone_rect = array((20, 7), 2)
        if start_zone_rect: pygame.draw.rect(self.screen, WHITE, start_zone_rect)
        if end_zone_rect: pygame.draw.rect(self.screen, WHITE, end_zone_rect)
        # Optionally draw thick border lines if they are purely visual
        # pygame.draw.line(self.screen, BLACK, (0, 0), (0, self.screen.get_height()), 15)
        # pygame.draw.line(self.screen, BLACK, (0, 0), (self.screen.get_width(), 0), 15)


        # 4. Circles
        pygame.draw.circle(self.screen, RED, self.circle1_center, CIRCLE_RADIUS)
        pygame.draw.circle(self.screen, BLUE, self.circle2_center, CIRCLE_RADIUS)

        # 5. Preview Line (if dragging)
        if self.dragging_circle is not None and self.is_mouse_button_down:
            can_draw_line, target_center_pos, _ = self.check_line_path()
            if target_center_pos: # Check if a valid target exists
                start_pos = self.circle1_center if self.dragging_circle == 1 else self.circle2_center
                line_color = RED if can_draw_line else BLUE # Red = OK, Blue = Blocked
                pygame.draw.line(self.screen, line_color, start_pos, target_center_pos, 3)

        # 6. Edit Mode Highlight
        if self.edit_mode_state == EDIT_STATE_SELECTED and self.edit_selection_pos:
            highlight_rect = array(self.edit_selection_pos, self.edit_selection_type if self.edit_selection_type else 1) # Get rect for pos
            if highlight_rect:
                 # Draw border highlight
                 pygame.draw.rect(self.screen, RED, highlight_rect, HIGHLIGHT_BORDER)
                 # Optionally, indicate type 1 vs 2 visually if needed


        # 7. Update Display (Usually done in the main loop)
        # pygame.display.flip() # Moved to main loop

# Example Main Loop Structure (main.py)
# import pygame
# from game import Game # Assuming this file is game.py
# from constants import WHITE # Need WHITE for screen fill
#
# pygame.init()
# screen_width = 800 # Or load from config
# screen_height = 600
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("Refactored Game")
#
# game = Game(screen)
# clock = pygame.time.Clock()
# running = True
#
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         game.handle_event(event) # Pass event to game object
#
#     # Game logic update (if any needed per frame beyond event handling)
#     # game.upda
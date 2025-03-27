import pygame
import sys
import math
import random # To initialize obstacles randomly

# Initialize Pygame
pygame.init()

# --- Constants ---
# Screen dimensions
WIDTH = 800
HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0) # Color for the marker
BLUE = (0, 0, 255) # Color for obstacles

# Scale factor (less relevant now, positioning is mainly in screen coordinates)
# SCALE = 20

# Number of radial lines to draw
NUM_RADIAL_LINES = 60 # Increased for better visual effect

# Small value to avoid division by zero or floating point issues
EPSILON = 1e-9

# --- Screen Setup ---
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Raycasting with Moving Obstacles") # Updated window title

# --- Obstacle Class ---
class Obstacle:
    """Represents a rectangular obstacle that moves and blocks rays."""
    def __init__(self, x, y, width, height, dx, dy):
        """
        Initializes an obstacle.
        Args:
            x (int): Initial top-left x-coordinate.
            y (int): Initial top-left y-coordinate.
            width (int): Width of the obstacle.
            height (int): Height of the obstacle.
            dx (float): Horizontal velocity (pixels per frame).
            dy (float): Vertical velocity (pixels per frame).
        """
        self.rect = pygame.Rect(x, y, width, height)
        self.dx = dx
        self.dy = dy
        self.color = BLUE

    def move(self):
        """Moves the obstacle and makes it bounce off screen edges."""
        self.rect.x += self.dx
        self.rect.y += self.dy

        # Bounce off vertical walls
        if self.rect.left < 0:
            self.rect.left = 0
            self.dx *= -1
        elif self.rect.right > WIDTH:
            self.rect.right = WIDTH
            self.dx *= -1

        # Bounce off horizontal walls
        if self.rect.top < 0:
            self.rect.top = 0
            self.dy *= -1
        elif self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            self.dy *= -1

    def draw(self, surface):
        """Draws the obstacle on the given surface."""
        pygame.draw.rect(surface, self.color, self.rect)


# --- Helper Functions ---

# logical_to_screen and screen_to_logical are less critical now as we mainly
# work in screen coordinates for raycasting, but keep them if needed elsewhere.
# def logical_to_screen(logical_x, logical_y): ...
# def screen_to_logical(screen_x, screen_y): ...


def cast_rays_with_obstacles(surface, center_pos_screen, num_lines, obstacles):
    """
    Casts rays outwards from a central point, stopping them at screen boundaries
    or the first obstacle they hit.
    Args:
        surface (pygame.Surface): The Pygame surface to draw on.
        center_pos_screen (tuple): The (x, y) screen coordinates for the ray origin.
        num_lines (int): How many rays to cast, evenly spaced around 360 degrees.
        obstacles (list): A list of Obstacle objects.
    """
    if num_lines <= 0: return
    angle_step_degrees = 360.0 / num_lines # Use float for precision
    center_x, center_y = center_pos_screen

    for i in range(num_lines):
        current_angle_degrees = i * angle_step_degrees
        angle_radians = math.radians(current_angle_degrees)

        # Direction vector (normalized)
        dx = math.cos(angle_radians)
        dy = math.sin(angle_radians)

        # --- Find the closest intersection point ---
        min_dist_sq = float('inf') # Use squared distance for comparison efficiency
        closest_point = None

        # 1. Check intersection with screen boundaries (walls)
        # Calculate distance 't' to each wall based on direction
        t_vals = []
        # Left Wall (x = 0)
        if abs(dx) > EPSILON and dx < 0: t = (0 - center_x) / dx; t_vals.append(t)
        # Right Wall (x = WIDTH)
        if abs(dx) > EPSILON and dx > 0: t = (WIDTH - center_x) / dx; t_vals.append(t)
        # Top Wall (y = 0)
        if abs(dy) > EPSILON and dy < 0: t = (0 - center_y) / dy; t_vals.append(t)
        # Bottom Wall (y = HEIGHT)
        if abs(dy) > EPSILON and dy > 0: t = (HEIGHT - center_y) / dy; t_vals.append(t)

        # Find the smallest positive distance 't' to a wall
        min_t_wall = float('inf')
        for t in t_vals:
            if t > EPSILON: # Check for positive distance
                min_t_wall = min(min_t_wall, t)

        # If a wall intersection was found, calculate the point and its squared distance
        if min_t_wall != float('inf'):
            wall_intersect_x = center_x + dx * min_t_wall
            wall_intersect_y = center_y + dy * min_t_wall
            dist_sq = (wall_intersect_x - center_x)**2 + (wall_intersect_y - center_y)**2
            if dist_sq < min_dist_sq:
                min_dist_sq = dist_sq
                closest_point = (wall_intersect_x, wall_intersect_y)


        # 2. Check intersection with each obstacle
        # Define a very long line segment starting from the center in the ray direction
        # Length needs to be longer than screen diagonal to ensure it crosses any potential obstacle
        max_ray_length = math.hypot(WIDTH, HEIGHT) * 1.1 # A bit longer than diagonal
        far_x = center_x + dx * max_ray_length
        far_y = center_y + dy * max_ray_length
        ray_segment = (center_pos_screen, (far_x, far_y))

        for obs in obstacles:
            # pygame.Rect.clipline returns the portion of the line inside the rect
            # returns () if no intersection
            clipped_line = obs.rect.clipline(ray_segment)

            if clipped_line: # If the ray intersects this obstacle
                # clipped_line gives (entry_point, exit_point) relative to the rect
                entry_point = clipped_line[0] # The first point where the ray hits the obstacle

                # Calculate squared distance from center to this entry point
                dist_sq = (entry_point[0] - center_x)**2 + (entry_point[1] - center_y)**2

                # If this intersection is closer than the current closest point (wall or other obstacle)
                if dist_sq < min_dist_sq:
                    min_dist_sq = dist_sq
                    closest_point = entry_point # Update the closest point

        # --- Draw the ray ---
        if closest_point:
            # Draw line from center to the closest intersection point found
            pygame.draw.line(surface, WHITE, center_pos_screen, (int(closest_point[0]), int(closest_point[1])), 1)
        # else: # Should not happen if walls are checked correctly unless center is outside screen
            # pass


# --- Create Obstacles ---
obstacles = []
num_obstacles = 5
for _ in range(num_obstacles):
    # Random initial position, size, and velocity
    w = random.randint(30, 80)
    h = random.randint(30, 80)
    x = random.randint(0, WIDTH - w)
    y = random.randint(0, HEIGHT - h)
    # Ensure obstacles don't start exactly on top of each other (simple check)
    # (More robust check would involve checking overlap with existing obstacles)
    vel_x = random.choice([-2, -1.5, -1, 1, 1.5, 2]) * random.uniform(0.8, 1.2)
    vel_y = random.choice([-2, -1.5, -1, 1, 1.5, 2]) * random.uniform(0.8, 1.2)
    obstacles.append(Obstacle(x, y, w, h, vel_x, vel_y))


# --- Main Game Loop ---
running = True
# Use screen coordinates directly for the marker now
marker_pos_screen = (WIDTH // 2, HEIGHT // 2) # Start marker at screen center

clock = pygame.time.Clock()

while running:
    # --- Event Handling ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            # Update marker position directly from mouse screen coordinates
            marker_pos_screen = event.pos

    # --- Game Logic ---
    # Move all obstacles
    for obs in obstacles:
        obs.move()

    # --- Drawing ---
    # Fill the background
    screen.fill(BLACK)

    # Ensure marker position is clamped within screen bounds
    # This is crucial because ray casting starts *from* this point.
    clamped_marker_x = max(0, min(WIDTH, marker_pos_screen[0]))
    clamped_marker_y = max(0, min(HEIGHT, marker_pos_screen[1]))
    clamped_marker_pos = (clamped_marker_x, clamped_marker_y)

    # 1. Draw the obstacles
    for obs in obstacles:
        obs.draw(screen)

    # 2. Cast rays from the clamped marker position
    cast_rays_with_obstacles(screen, clamped_marker_pos, NUM_RADIAL_LINES, obstacles)

    # 3. Draw the marker (ray source) on top
    pygame.draw.circle(screen, RED, clamped_marker_pos, 5)

    # --- Update Display ---
    pygame.display.flip()

    # --- Frame Rate Control ---
    clock.tick(60) # Limit frame rate to 60 FPS

# --- Cleanup ---
pygame.quit()
sys.exit()
import OpenGL.GL as gl
import OpenGL.GLUT as glut
import OpenGL.GLU as glu
import math
import random

# Global variables
falling_leaves = []
is_falling = False
is_paused = False
leaf_positions = []
current_season = 1  # 1: Summer, 2: Rainy, 3: Winter
raindrops = []
snowflakes = []
leaf_fall_timer = 0
leaf_fall_interval = 10  # Reduced interval for faster leaf falling
is_day = True  # New variable for day/night mode

class Leaf:
    def __init__(self, x, y, season):
        self.x = x
        self.y = y
        self.speed = random.uniform(1.0, 2.0)  # Increased speed for faster falling
        self.swing = random.uniform(-1, 1)
        self.season = season
        self.set_color()

    def set_color(self):
        if self.season == 1:  # Summer
            self.start_color = [0.0, 0.8, 0.0]  # Bright green
            self.end_color = [0.5, 0.8, 0.5]  # Light green
        elif self.season == 2:  # Rainy
            self.start_color = [0.0, 0.5, 0.0]  # Dark green
            self.end_color = [0.0, 0.8, 0.0]  # Bright green
        else:  # Winter
            self.start_color = [1.0, 0.75, 0.8]  # Pink
            self.end_color = [1.0, 0.65, 0.0]  # Orange
        self.color = self.start_color.copy()

    def update(self):
        if not is_paused:
            self.y -= self.speed
            self.x += math.sin(self.y / 20) * self.swing

            # Change color gradually as it falls
            if self.y > 100:
                fall_progress = (600 - self.y) / 500
                for i in range(3):
                    self.color[i] = self.start_color[i] + (self.end_color[i] - self.start_color[i]) * fall_progress

        return self.y > 100

class Raindrop:
    def __init__(self):
        self.x = random.randint(0, 800)
        self.y = 600
        self.speed = random.uniform(5, 10)

    def update(self):
        if not is_paused:
            self.y -= self.speed
            self.x -= self.speed * 0.5  # Add horizontal movement for slanted rain
        return self.y > 0

class Snowflake:
    def __init__(self):
        self.x = random.randint(0, 800)
        self.y = 600
        self.speed = random.uniform(1, 3)
        self.swing = random.uniform(-1, 1)

    def update(self):
        if not is_paused:
            self.y -= self.speed
            self.x += math.sin(self.y / 50) * self.swing
        return self.y > 0

def init():
    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glLoadIdentity()
    glu.gluOrtho2D(0, 800, 0, 600)

def draw_pixel(x, y):
    gl.glBegin(gl.GL_POINTS)
    gl.glVertex2f(x, y)
    gl.glEnd()

def midpoint_line(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    x, y = x1, y1

    x_inc = 1 if x2 > x1 else -1
    y_inc = 1 if y2 > y1 else -1

    if dx > dy:
        p = 2 * dy - dx
        for _ in range(dx):
            draw_pixel(x, y)
            if p >= 0:
                y += y_inc
                p -= 2 * dx
            x += x_inc
            p += 2 * dy
    else:
        p = 2 * dx - dy
        for _ in range(dy):
            draw_pixel(x, y)
            if p >= 0:
                x += x_inc
                p -= 2 * dy
            y += y_inc
            p += 2 * dx
    draw_pixel(x, y)

def midpoint_circle(center_x, center_y, radius):
    x, y = 0, radius
    p = 1 - radius

    def plot_circle_points(cx, cy, x, y):
        draw_pixel(cx + x, cy + y)
        draw_pixel(cx - x, cy + y)
        draw_pixel(cx + x, cy - y)
        draw_pixel(cx - x, cy - y)
        draw_pixel(cx + y, cy + x)
        draw_pixel(cx - y, cy + x)
        draw_pixel(cx + y, cy - x)
        draw_pixel(cx - y, cy - x)

    while x <= y:
        plot_circle_points(center_x, center_y, x, y)
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1

def draw_tree(x, y, length, angle, depth):
    if depth > 0:
        x2 = x + length * math.cos(math.radians(angle))
        y2 = y + length * math.sin(math.radians(angle))

        # Draw branch
        gl.glColor3f(0.545, 0.271, 0.075)
        midpoint_line(int(x), int(y), int(x2), int(y2))

        # Store leaf positions at terminal branches
        if depth == 1:
            leaf_positions.append((int(x2), int(y2)))
            if not is_falling:  # Only draw leaves if they haven't started falling
                if current_season == 1:
                    gl.glColor3f(0.0, 0.8, 0.0)  # Bright green for summer
                elif current_season == 2:
                    gl.glColor3f(0.0, 0.5, 0.0)  # Dark green for rainy season
                else:
                    gl.glColor3f(1.0, 0.75, 0.8)  # Pink for winter
                midpoint_circle(int(x2), int(y2), 3)

        new_length = length * 0.7
        draw_tree(x2, y2, new_length, angle - 30, depth - 1)
        draw_tree(x2, y2, new_length, angle + 30, depth - 1)

def draw_ground():
    gl.glColor3f(0.0, 0.8, 0.0)
    gl.glBegin(gl.GL_QUADS)
    gl.glVertex2f(0, 0)
    gl.glVertex2f(800, 0)
    gl.glVertex2f(800, 100)
    gl.glVertex2f(0, 100)
    gl.glEnd()

def draw_falling_leaves():
    for leaf in falling_leaves:
        gl.glColor3f(leaf.color[0], leaf.color[1], leaf.color[2])
        midpoint_circle(int(leaf.x), int(leaf.y), 3)

def draw_rain():
    gl.glColor3f(0.5, 0.5, 1.0)  # Light blue for rain
    gl.glLineWidth(2.0)  # Increased line width for larger raindrops
    gl.glBegin(gl.GL_LINES)
    for raindrop in raindrops:
        gl.glVertex2f(raindrop.x, raindrop.y)
        gl.glVertex2f(raindrop.x - 5, raindrop.y - 10)  # Slanted rain
    gl.glEnd()

def draw_snow():
    gl.glColor3f(1.0, 1.0, 1.0)  # White for snow
    gl.glPointSize(5.0)  # Increased point size for larger snowflakes
    gl.glBegin(gl.GL_POINTS)
    for snowflake in snowflakes:
        gl.glVertex2f(snowflake.x, snowflake.y)
    gl.glEnd()

def update_falling_leaves():
    global falling_leaves, leaf_fall_timer
    if not is_paused and is_falling:
        falling_leaves = [leaf for leaf in falling_leaves if leaf.update()]
        
        # Add new leaves one by one
        leaf_fall_timer += 1
        if leaf_fall_timer >= leaf_fall_interval and leaf_positions:
            x, y = leaf_positions.pop(random.randint(0, len(leaf_positions) - 1))
            falling_leaves.append(Leaf(x, y, current_season))
            leaf_fall_timer = 0

def update_rain():
    global raindrops
    if not is_paused:
        raindrops = [raindrop for raindrop in raindrops if raindrop.update()]
        if len(raindrops) < 200:
            raindrops.append(Raindrop())

def update_snow():
    global snowflakes
    if not is_paused:
        snowflakes = [snowflake for snowflake in snowflakes if snowflake.update()]
        if len(snowflakes) < 100:
            snowflakes.append(Snowflake())

def mouse_click(button, state, x, y):
    global is_falling
    if button == glut.GLUT_LEFT_BUTTON and state == glut.GLUT_DOWN:
        is_falling = True

def keyboard(key, x, y):
    global is_paused, is_falling, falling_leaves, current_season, raindrops, snowflakes, leaf_positions, is_day
    if key == b' ':
        is_paused = not is_paused  # Toggle pause
    elif key == b'r' or key == b'R':
        is_paused = False
        is_falling = False
        falling_leaves.clear()
        raindrops.clear()
        snowflakes.clear()
        leaf_positions.clear()
    elif key in [b'1', b'2', b'3']:
        current_season = int(key)
        is_falling = False
        falling_leaves.clear()
        raindrops.clear()
        snowflakes.clear()
        leaf_positions.clear()
    elif key == b'd' or key == b'D':
        is_day = True
    elif key == b'n' or key == b'N':
        is_day = False

def display():
    if is_day:
        gl.glClearColor(0.529, 0.808, 0.922, 1.0)  # Sky blue for day
    else:
        gl.glClearColor(0.1, 0.1, 0.3, 1.0)  # Dark blue for night

    gl.glClear(gl.GL_COLOR_BUFFER_BIT)

    draw_ground()

    gl.glPointSize(2.0)
    draw_tree(600, 100, 100, 90, 9)

    if is_falling:
        draw_falling_leaves()
        update_falling_leaves()

    if current_season == 2:  # Rainy season
        draw_rain()
        update_rain()
    elif current_season == 3:  # Winter
        draw_snow()
        update_snow()

    glut.glutSwapBuffers()

def timer(value):
    glut.glutPostRedisplay()
    glut.glutTimerFunc(16, timer, 0)  # 60 FPS approximately

def main():
    glut.glutInit()
    glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGB)
    glut.glutInitWindowSize(800, 600)
    glut.glutCreateWindow(b"Seasonal Tree Animation")

    init()
    glut.glutDisplayFunc(display)
    glut.glutMouseFunc(mouse_click)
    glut.glutKeyboardFunc(keyboard)
    glut.glutTimerFunc(0, timer, 0)
    glut.glutMainLoop()

if __name__ == "__main__":
    main()
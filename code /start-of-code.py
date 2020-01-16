import arcade 
import random
import math

WIDTH = 640
HEIGHT = 480

# player variables

player_x = WIDTH/2
player_y = HEIGHT/2 

player_w = []
player_l = []

#rock variables 
rock_x_pos = []
rock_y_pos = []
rock_radius = []

#the score variables 
timer = 0
current_score = 0

#images 
truck_img = arcade.load_texture('images/truck.png')
rock_img = arcade.load_texture()
palm_tree_img = arcade.load_texture('images/palm tree.png')
trench_img = arcade.load_texture('images/trench.png')
game_background = arcade.load_texture()
w_key_img = arcade.load_texture('images/W_key.png')
s_key_img = arcade.load_texture('images/S_key.png')
a_key_img = arcade.load_texture('images/A_key.png')
d_key_img = arcade.load_texture('images/D_key.png')
pause_img = arcade.load_texture('images/pause.png')

#health bar variables 
player_health = 100
player_max_health = 100 
player_alvie = True 

#truck movements 
up_pressed = False 
down_pressed = False 
left_pressed = False 
right_pressed = False 

#pause button on game screen 
button_pause = [WIDTH/2, 250, 125, 40, False, arcade.color.BROWN_NOSE, arcade.color.BROWN]
BTN_pause_X = 0 
BTN_pause_Y = 1 
BTN_pasue_WIDTH = 2
BTN_pause_HEIGHT = 3 
BTN_pause_IS_CLICKED = 4 
BTN_pause_COLOR = 5 
BTN_pause_COLOR_CLICKED = 6

#pause screen button back to game screen 
button_pause_screen = [WIDTH / 2, 250, 125, 40, False, arcade.color.BROWN_NOSE, arcade.color.BROWN]
BTN_pause_screen_X = 0
BTN_pause_screen_Y = 1
BTN_pasue_WIDTH = 2
BTN_pause_HEIGHT = 3
BTN_pause_IS_CLICKED = 4
BTN_pause_COLOR = 5
BTN_pause_COLOR_CLICKED = 6

#end screen button 
button_end = [WIDTH / 2, 250, 125, 40, False, arcade.color.BROWN_NOSE, arcade.color.BROWN]
BTN_end_X = 0 
BTN_end_Y = 1
BTN_end_WIDTH = 2
BTN_end_HEIGHT = 3
BTN_end_IS_CLICKED = 4
BTN_end_COLOR = 5
BTN_end_COLOR_CLICKED = 6

#menu screen button on pause screen 
button_menu = [WIDTH / 2, 250, 125, 40, False, arcade.color.BROWN_NOSE, arcade.color.BROWN]
BTN_menu_X = 0
BTN_menu_Y = 1
BTN_menu_WIDTH = 2
BTN_menu_HEIGHT = 3
BTN_menu_IS_CLICKED = 4
BTN_menu_COLOR = 5
BTN_menu_COLOR_CLICKED = 6

#start button variables 
button_end = [WIDTH / 2, 250, 125, 40, False, arcade.color.BROWN_NOSE, arcade.color.BROWN]
BTN_end_X = 0
BTN_end_Y = 1
BTN_end_WIDTH = 2
BTN_end_HEIGHT = 3
BTN_end_IS_CLICKED = 4
BTN_end_COLOR = 5
BTN_end_COLOR_CLICKED = 6

#instructions button variables 
button3 = [WIDTH / 2, 325, 125, 40, False, arcade.color.BROWN_NOSE, arcade.color.BRONZE]
BTN_3_X = 0
BTN_3_Y = 1
BTN_3_WIDTH = 2
BTN_3_HEIGHT = 3
BTN_3_IS_CLICKED = 4
BTN_3_COLOR = 5
BTN_3_COLOR_CLICKED = 6

#screen variables 
current_screen = "menu"

def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.DARK_MOSS_GREEN)
    arcade.schedule(update, 1/60)

    window = arcade.get_window()
    window.on_draw = on_draw 
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press
    window.on_mouse_release = on_mouse_release

    arcade.run()

def update(delta_time):
    global player_health, player_y, player_x, player_alvie
    global current_screen
    global up_pressed, down_pressed, left_pressed, right_pressed
    global rock_x_pos, rock_y_pos, rock_radius
    global player_w, player_l
    global timer 

# Player Movment
    if up_pressed == True:
        player_y += 10 
    if down_pressed == True:
        player_y -= 10 
    global player_x
    if left_pressed == True:
        player_x -= 10 
    if right_pressed == True:
        player_x += 10 

#Rocks
    for index in range(len(rock_y_pos)):
        rock_y_pos[index] -= 6 
        if rock_y_pos[index] < 0:
            rock_y_pos[index] = random.randrange(HEIGHT, HEIGHT + 50)
            rock_x_pos[index] = random.randrange(0, WIDTH)
    
#rock collisions     
    for i, (x, y) in enumerate(zip(rock_x_pos, rock_y_pos)):
        a = x - player_x
        b = y - player_y
        distance = math.sqrt(a**2 + b**2)
        if distance - 30 - 70 <= 0 and current_screen == "game":
            player_health -= 25 
            del rock_x_pos[i]
            del rock_y_pos[i]

#score update 
if current_screen == "game":
    timer += 0.5 
elif current_screen == "menu":
    timer += 0 
elif current_screen == "instructions":
    timer += 0 
elif current_screen == "End":
    timer += 0 
elif current_screen == "pause":
    timer += 0 
elif
        
#Player Health Update
if player_health == 0:
    player_alive = False

if player_alive == False:
    current_screen = "End"

# The Boundaries
if player_y >= 480:
    up_pressed = False

if player_y <= 0:
    down_pressed = False

if player_x <= 0:
    left_pressed = False

if player_x <= 635:
    right_pressed = False    





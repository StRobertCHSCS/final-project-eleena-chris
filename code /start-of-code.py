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

#big rocks 
rock_big_x_pos = []
rock_big_y_pos = []

#the score variables 
timer = 0
current_score = 0

#images 
truck_img = arcade.load_texture('images/truck.png')
rock_img = arcade.load_texture()
palm_tree_img = arcade.load_texture('images/palm tree.png')
trench_img = arcade.load_texture('images/trench.png')
game_background = arcade.load_texture()
w_key_img = 
s_key_img = 
a_key_img = 
d_key_img = 
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
BTN_pause = 

#pause screen button back to game screen 

#end screen button 

#menu screen button on pause screen 

#start button variables 

#instructions button variables 

#screen variables 
current_screen = "menu"

def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.DARK_MOSS_GREEN)
    arcade.schedule(update, 1/60)

    
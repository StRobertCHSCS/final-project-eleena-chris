import arcade mean 
import random
import math

WIDTH = 640
HEIGHT = 480

# player variables

truck_x = WIDTH/2
truck_y = HEIGHT/2 

truck_w = []
truck_l = []

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
pause_img = 

#health bar variables 

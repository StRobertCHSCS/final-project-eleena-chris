import arcade
import random
import math

WIDTH = 640
HEIGHT = 480

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
button_pause = [WIDTH/2, 250, 125, 40, False, arcade.color.BROWN_NOSE, arcade.color.BROWN_NOSE]
BTN_pause_X = 0 
BTN_pause_Y = 1 
BTN_pasue_WIDTH = 2
BTN_pause_HEIGHT = 3 
BTN_pause_IS_CLICKED = 4

#pause screen button back to game screen 

#end screen button 

#menu screen button on pause screen 

#start button variables 

#instructions button variables 

# Screen Variable
current_screen = "menu"



def setup():
   arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
   arcade.set_background_color(arcade.color.DARK_BLUE)
   arcade.schedule(update, 1 / 60)

   # Override arcade window methods
   window = arcade.get_window()
   window.on_draw = on_draw
   window.on_key_press = on_key_press
   window.on_key_release = on_key_release
   window.on_mouse_press = on_mouse_press
   window.on_mouse_release = on_mouse_release

   arcade.run()


def update(delta_time):
   global player_health, player_y, player_x, player_alive
   global current_screen
   global up_pressed, down_pressed, left_pressed, right_pressed
   global ast_x_pos, ast_y_pos, ast_radius
   global ship_l, ship_w
   global ast_big_y_pos, ast_big_x_pos
   global timer

   # Player Movement Update
   if up_pressed == True:
       player_y += 10
   if down_pressed == True:
       player_y -= 10
   global player_x
   if left_pressed == True:
       player_x -= 10
   if right_pressed == True:
       player_x += 10

   # Asteroids
   for index in range(len(ast_y_pos)):
       ast_y_pos[index] -= 6

       if ast_y_pos[index] < 0:
           ast_y_pos[index] = random.randrange(HEIGHT, HEIGHT + 50)
           ast_x_pos[index] = random.randrange(0, WIDTH)
   for index in range(len(ast_big_y_pos)):
       ast_big_y_pos[index] -= 2

       if ast_big_y_pos[index] < 0:
           ast_big_y_pos[index] = random.randrange(HEIGHT, HEIGHT + 50)
           ast_big_x_pos[index] = random.randrange(0, WIDTH)

   # Asteroid Collisions
   for i, (x, y) in enumerate(zip(ast_x_pos, ast_y_pos)):
       a = x - player_x
       b = y - player_y
       distance = math.sqrt(a ** 2 + b ** 2)

       if distance - 30 - 70 <= 0 and current_screen == "game":
           player_health -= 25
           del ast_x_pos[i]
           del ast_y_pos[i]
   for i, (x, y) in enumerate(zip(ast_big_x_pos, ast_big_y_pos)):
       a = x - player_x
       b = y - player_y
       distance = math.sqrt(a ** 2 + b ** 2)

       if distance - 30 - 30 <= 0 and current_screen == "game":
           player_health -= 25
           del ast_big_x_pos[i]
           del ast_big_y_pos[i]

   # Score Update
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

   # Player Health Update
   if player_health == 0:
       player_alive = False

   if player_alive == False:
       current_screen = "End"

   # The boundaries

   if player_y >= 480:
       up_pressed = False

   if player_y <= 0:
       down_pressed = False

   if player_x <= 0:
       left_pressed = False

   if player_x >= 635:
       right_pressed = False



def on_draw():
   arcade.start_render()
   global current_screen
   global player_x, player_y, ast_big_y_pos, ast_big_x_pos, ast_x_pos, ast_y_pos
   global player_alive, player_health
   global timer, current_score
   arcade.start_render()
   # Draw in here...

   x = 180
   y = 325

   # Main Menu
   if current_screen == "menu":
       arcade.set_background_color(arcade.color.WHITE)
       arcade.draw_texture_rectangle(x, y, 1000, 645, game_background)
       if button2[BTN_2_IS_CLICKED]:
           color = button2[BTN_2_COLOR_CLICKED]
       else:
           color = button2[BTN_2_COLOR]

       if button3[BTN_3_IS_CLICKED]:
           color = button3[BTN_3_COLOR_CLICKED]
       else:
           color = button3[BTN_3_COLOR]

       arcade.draw_rectangle_filled(button2[BTN_2_X], button2[BTN_2_Y], 150, button2[BTN_2_HEIGHT], arcade.color.EARTH_YELLOW)
       arcade.draw_rectangle_filled(button3[BTN_3_X], button3[BTN_3_Y], button3[BTN_3_WIDTH], button3[BTN_3_HEIGHT], arcade.color.YELLOW)
       arcade.draw_text("INSTRUCTIONS", 170, 245, arcade.color.BLACK, 16, 300, "center", 'arial', True, False)
       arcade.draw_text("START", 165, 310, arcade.color.BLACK, 25, 300, "center", 'arial', True, False)
       arcade.draw_text("READY, SET, LIFTOFF!", 65, 420, arcade.color.RED_ORANGE, 35, 500, "center", 'arial', True, False)
       arcade.draw_line(90, 410, 550, 410, arcade.color.RED_ORANGE, 8)
       arcade.draw_texture_rectangle(90, 220, 100, 300, ship_img)
       arcade.draw_texture_rectangle(520, 220, 100, 300, ship_img)

   # Instructions Screen
   elif current_screen == "instructions":
       arcade.set_background_color(arcade.color.COOL_BLACK)
       player_alive = True
       arcade.draw_text("INSTRUCTIONS", 230, 400, arcade.color.WHITE, 50, 800, "left", "Veneer", True, False)
       arcade.draw_line(120, 390, 500, 390, arcade.color.WHITE, 10)
       arcade.draw_texture_rectangle(320, 250, 60, 60, W_key_img)
       arcade.draw_texture_rectangle(320, 180, 60, 60, S_key_img)
       arcade.draw_texture_rectangle(250, 180, 60, 60, A_key_img)
       arcade.draw_texture_rectangle(390, 180, 60, 60, D_key_img)
       arcade.draw_text("UP", 305, 290, arcade.color.WHITE, 30, 150, "left", 'arial', True, False)
       arcade.draw_text("DOWN", 300, 110, arcade.color.WHITE, 30, 200, "left", 'arial', True, False)
       arcade.draw_text("LEFT", 170, 160, arcade.color.WHITE, 30, 200, "left", 'arial', True, False)
       arcade.draw_text("RIGHT", 430, 160, arcade.color.WHITE, 30, 200, "left", 'arial', True, False)
       arcade.draw_text("Press M to return to Menu", 5, 320, arcade.color.WHITE, 14, 300, "center", "Veneer", True, False)
       arcade.draw_text("Try to avoid the asteroids", 5, 280, arcade.color.WHITE, 14, 300, "center", "Veneer", True, False)

   # Pause Screen
   elif current_screen == "pause":
       arcade.set_background_color(arcade.color.BLACK)
       arcade.draw_text("PAUSE", 40, 375, arcade.color.WHITE, 50, 800, "left", "Veneer", True, False)
       arcade.draw_line(40, 360, 600, 360, arcade.color.WHITE, 10)
       if button_pause_screen[BTN_pause_screen_IS_CLICKED]:
           color = button_pause_screen[BTN_pause_screen_COLOR_CLICKED]
       else:
           color = button_pause_screen[BTN_pause_screen_COLOR]

       if button_menu[BTN_menu_IS_CLICKED]:
           color = button_menu[BTN_menu_COLOR_CLICKED]
       else:
           color = button_menu[BTN_menu_COLOR]

       arcade.draw_rectangle_filled(320, 240, 126, 40, arcade.color.EARTH_YELLOW)
       arcade.draw_rectangle_filled(320, 180, 126, 40, arcade.color.GREEN)
       arcade.draw_text("Resume", 170, 225, arcade.color.BLACK, 28, 300, "center", 'arial', True, False)
       arcade.draw_text("Main Menu", 170, 165, arcade.color.BLACK, 20, 300, "center", 'arial', True, False)
       arcade.draw_text(f"Current Score: {timer}", 170, 120, arcade.color.WHITE, 18, 300, "center", 'arial', True, False)

   # Game Screen
   elif current_screen == "game":
       arcade.draw_texture_rectangle(x, y, 1300, 645, game_background)
       arcade.set_background_color(arcade.color.WHITE)
       pause_screen()
       arcade.draw_texture_rectangle(player_x, player_y, ship_w[0], ship_l[0], ship_img)
       arcade.draw_text(f"SCORE: {timer}", 70, 450, arcade.color.WHITE, 12, 300, "left", "", True)
       for x, y in zip(ast_x_pos, ast_y_pos):
           arcade.draw_texture_rectangle(x, y, ast_radius[0], 40,  ast_img)
       for x, y in zip(ast_big_x_pos, ast_big_y_pos):
           arcade.draw_texture_rectangle(x, y, ast_radius[0], 80, ast_img)
       max_bar_width = 170
       bar_height = 40
       health_pos_x = WIDTH - max_bar_width
       health_pos_y = HEIGHT - bar_height

       arcade.draw_xywh_rectangle_filled(WIDTH - max_bar_width, HEIGHT - bar_height, max_bar_width, bar_height, arcade.color.BLACK)
       pass

       health_width = player_health / player_max_health * max_bar_width

       arcade.draw_xywh_rectangle_filled(WIDTH - max_bar_width, HEIGHT - bar_height, max_bar_width, bar_height, arcade.color.WHITE)
       if player_health == 100:
           arcade.draw_xywh_rectangle_filled(health_pos_x, health_pos_y, max_bar_width, bar_height, arcade.color.GREEN)
           arcade.draw_text("100/100", 500, health_pos_y, arcade.color.BLACK, font_size=20)
       elif player_health == 75:
           arcade.draw_xywh_rectangle_filled(health_pos_x, health_pos_y, 130, 40, arcade.color.GREEN_YELLOW)
           arcade.draw_text("75/100", 500, health_pos_y, arcade.color.BLACK, font_size=20)
       elif player_health == 50:
           arcade.draw_xywh_rectangle_filled(health_pos_x, health_pos_y, 85, 40, arcade.color.YELLOW)
           arcade.draw_text("50/100", 500, health_pos_y, arcade.color.BLACK, font_size=20)
       elif player_health == 25:
           arcade.draw_xywh_rectangle_filled(health_pos_x, health_pos_y, 45, 40, arcade.color.RED)
           arcade.draw_text("25/100", 500, health_pos_y, arcade.color.BLACK, font_size=20)

       if player_health == 0:
           current_screen = "End"

   # Game Over Screen
   elif current_screen == "End":
       arcade.set_background_color(arcade.color.BLACK)
       current_score = timer
       arcade.draw_text("GAME OVER", 230, 400, arcade.color.WHITE, 50, 800, "left", "Veneer", True, False)
       arcade.draw_line(120, 390, 500, 390, arcade.color.WHITE, 10)
       arcade.draw_text(f"Your Score was {current_score}", 250, 150, arcade.color.WHITE, 20, 800, "left", "arial", True, False)

       if button_end[BTN_end_IS_CLICKED]:
           color = button_end[BTN_end_COLOR_CLICKED]
       else:
           color = button_end[BTN_end_COLOR]

       arcade.draw_rectangle_filled(320, 240, 126, 40, arcade.color.EARTH_YELLOW)
       arcade.draw_text("Restart", 170, 225, arcade.color.BLACK, 28, 300, "center", 'arial', True, False)
       arcade.draw_texture_rectangle(90, 210, 100, 290, ship_img)
       arcade.draw_texture_rectangle(520, 210, 100, 290, ship_img)
       for i, (x, y) in enumerate(zip(ast_x_pos, ast_y_pos)):
           a = x - player_x
           b = y - player_y
           distance = math.sqrt(a ** 2 + b ** 2)

           if distance - 30 - 70 <= 0 and current_screen == "game":
               player_health -= 25
               del ast_x_pos[i]
               del ast_y_pos[i]
       for i, (x, y) in enumerate(zip(ast_big_x_pos, ast_big_y_pos)):
           a = x - player_x
           b = y - player_y
           distance = math.sqrt(a ** 2 + b ** 2)

           if distance - 30 - 30 <= 0 and current_screen == "game":
               player_health -= 25
               del ast_big_x_pos[i]
               del ast_big_y_pos[i]
       player_health = 100



def on_key_press(key, modifiers):
   global current_screen, timer

   # Instructions Key
   if current_screen == "instructions":
       if key == arcade.key.M:
           current_screen = "menu"

   # Secret Menu Key
   elif current_screen == "menu":
      if key == arcade.key.R:
           current_screen = "End"

   # Game Screen Keys
   elif current_screen == "game":
       global up_pressed
       if key == arcade.key.W:
           up_pressed = True
       global down_pressed
       if key == arcade.key.S:
           down_pressed = True
       global left_pressed
       if key == arcade.key.A:
           left_pressed = True
       global right_pressed
       if key == arcade.key.D:
           right_pressed = True


def on_key_release(key, modifiers):
   global current_screen

   # Player Movement Key
   if current_screen == "game":
       global up_pressed
       if key == arcade.key.W:
           up_pressed = False
       global down_pressed
       if key == arcade.key.S:
           down_pressed = False
       global left_pressed
       if key == arcade.key.A:
           left_pressed = False
       global right_pressed
       if key == arcade.key.D:
           right_pressed = False


def on_mouse_press(x, y, button, modifiers):
   global current_screen

   # Menu Screen Buttons
   if current_screen == "menu":
       if x > 257 and x < 383 and y > 305 and y < 345:
           current_screen = "game"
       if x > 257 and x < 383 and y > 230 and y < 270:
           current_screen = "instructions"

   # Pause Button on Game Screen
   if current_screen == "game":
       if x > 0 and x < 60 and y > 420 and y < 480:
           current_screen = "pause"

   # Pause Screen Buttons
   if current_screen == "pause":
       if x > 245 and x < 420 and y > 220 and y < 270:
           current_screen = "game"
       if x > 245 and x < 420 and y > 140 and y < 180:
           current_screen = "menu"

   # End Screen Button
   if current_screen == "End":
       if x > 310 and x < 446 and y > 200 and y < 240:
           current_screen = "menu"


def on_mouse_release(x, y, button, modifiers):
   global current_screen

   # Button Release
   button2[BTN_2_IS_CLICKED] = False
   button3[BTN_3_IS_CLICKED] = False
   button_pause[BTN_pause_IS_CLICKED] = False
   button_pause_screen[BTN_pause_screen_IS_CLICKED] = False
   button_menu[BTN_menu_IS_CLICKED] = False
   button_end[BTN_end_IS_CLICKED] = False


def pause_screen():
   if button_pause[BTN_pause_IS_CLICKED]:
       color = button_pause[BTN_pause_IS_CLICKED]
   else:
       color = button_pause[BTN_pause_COLOR]

   arcade.draw_rectangle_filled(20, 460, 40, 40, arcade.color.EARTH_YELLOW)
   arcade.draw_texture_rectangle(20, 460, 40, 40, pause_img)


if __name__ == '__main__':
   setup()

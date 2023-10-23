import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import winsound
from random import randrange
from random import randint, choice
import pygame
import threading 



# Create the Tkinter window
window = tk.Tk()
window.title('Deepdive-Game')
window.attributes('-fullscreen', True)

SCREEN_WIDTH = 3000
SCREEN_HEIGHT = 900

GRAVITY_FORCE = 9
JUMP_FORCE = 100
SPEED = 7

TIMED_LOOP = 10

# ------------- Variables ---------------------

frame = tk.Frame(window, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
frame.pack()

canvas = tk.Canvas(frame, width=SCREEN_WIDTH, height=SCREEN_HEIGHT,  scrollregion= (0,0,4000,5000))
canvas.pack()

#.....score......
score = 0

#scrollbar
scrollbar_bottom = tk.Scrollbar(window, orient='horizontal', command=canvas.xview)
canvas.configure(xscrollcommand=scrollbar_bottom.set)
scrollbar_bottom.place(relx=0, rely=1, relwidth=1, anchor='sw')

#create image

bom_image = Image.open('images/bom.png')
bom_resize = bom_image.resize((70,70))
img_bom =ImageTk.PhotoImage(bom_resize)

bom2_image = Image.open('images/bom2.png')
img_bom2 =ImageTk.PhotoImage(bom2_image)

bg1_image = Image.open('images/bg1.png')
img_bg1 =ImageTk.PhotoImage(bg1_image)

#Create image bubble water

image_bubble_list = []
for i in range(50):
    bubble1_image = Image.open('images/bubbles/bubble1.png')
    bubble1 = ImageTk.PhotoImage(bubble1_image)
    image_bubble_list.append(bubble1)
    
# Iterate over the list of PhotoImage objects and create a create_image() item for each image.
x=0
y=0
for image in image_bubble_list:
    canvas.create_image(x, y, image=image, tag="BUBBLE")
    x+=100
    y+=100
    
# Function to update the object's position
def update_position_down():
    bubble_coods = canvas.coords('BUBBLE')

    if bubble_coods[1]< 700:
        canvas.move('BUBBLE', 0, 3)
        
        window.after(50, update_position_down)
    else:
        update_position_up()

def update_position_up():
    bubble_coods = canvas.coords('BUBBLE')
    if bubble_coods[1]> -200 :
        canvas.move('BUBBLE', 0, -2)
        window.after(30, update_position_up)
    else:
        update_position_down()

window.after(30, update_position_up)




#group fish image

image_fish_list = []
for i in range(1,8):
    fish_image = Image.open('images/fishes/fish'+str(i)+'.gif')
    fish_resize = fish_image.resize((100,100))
    img_fish =ImageTk.PhotoImage(fish_resize)
    image_fish_list.append(img_fish)
    
# Iterate over the list of PhotoImage objects and create a create_image() item for each image.
x=10
y=10
for fish in image_fish_list:
    canvas.create_image(x, y, image=fish, tag="FISH")
    x+=300
    y+=200


#group dimond image

dimond1_image = Image.open('images/dimond/dimond.gif')
dimond1_resize = dimond1_image.resize((50,60))
img_dimond1 =ImageTk.PhotoImage(dimond1_resize)

dimond2_image = Image.open('images/dimond/dimond2.gif')
dimond2_resize = dimond2_image.resize((30,40))
img_dimond2 =ImageTk.PhotoImage(dimond2_resize)

#..........box.........

box1_image = Image.open('images/box/box.png')
box1_resize = box1_image.resize((60,60))
img_box1 =ImageTk.PhotoImage(box1_resize)




#grass image

grass1_image = Image.open('images/grasses/grass1.gif')
grass1_resize = grass1_image.resize((100,300))
img_grass1 =ImageTk.PhotoImage(grass1_resize)

grass2_image = Image.open('images/grasses/grass1.gif')
grass2_resize = grass2_image.resize((100,300))
img_grass2 =ImageTk.PhotoImage(grass2_resize)

grass3_image = Image.open('images/grasses/grass1.gif')
grass3_resize = grass3_image.resize((100,250))
img_grass3 =ImageTk.PhotoImage(grass3_resize)


grass4_image = Image.open('images/grasses/grass4.png')
grass4_resize = grass4_image.resize((100,100))
img_grass4 =ImageTk.PhotoImage(grass4_resize)

grass6_image = Image.open('images/grasses/grass6.gif')
grass6_resize = grass6_image.resize((200,150))
img_grass6 =ImageTk.PhotoImage(grass6_resize)

grass7_image = Image.open('images/grasses/grass7.png')
grass7_resize = grass7_image.resize((200,150))
img_grass7 =ImageTk.PhotoImage(grass7_resize)

#stones image
stone1_image = Image.open('images/stones/stone1.png')
stone1_resize = stone1_image.resize((80,70))
img_stone1 =ImageTk.PhotoImage(stone1_resize)

stone2_image = Image.open('images/stones/stone2.png')
stone2_resize = stone2_image.resize((80,70))
img_stone2 =ImageTk.PhotoImage(stone2_resize)

stone3_image = Image.open('images/stones/stone3.png')
stone3_resize = stone3_image.resize((80,70))
img_stone3 =ImageTk.PhotoImage(stone3_resize)

#image flag
flag_image = Image.open('images/flag.png')
flag_resize = flag_image.resize((80,90))
img_flag =ImageTk.PhotoImage(flag_resize)

#create canvas image bg
canvas.create_image(600,300, image =img_bg1)
canvas.create_image(1800,300, image =img_bg1)
canvas.create_image(3000,300, image =img_bg1)
canvas.create_image(4000,300, image =img_bg1)
flag_id = canvas.create_image(3900, 670, image = img_flag)


#canvas image border bottom
image_list = []
for i in range(11):
    border_bottom_image = Image.open('images/border_bottom.jpg')
    img_bottom= ImageTk.PhotoImage(border_bottom_image)
    image_list.append(img_bottom)

# Iterate over the list of PhotoImage objects and create a create_image() item for each image.
x=0
y=750
for img in image_list:
    canvas.create_image(x, y, image=img, tag="PLATFORM")
    x+=400



# Create a falling object (boms)
bom_id = canvas.create_image(190, 200, image = img_bom, tags= 'BOM')
bom2_id = canvas.create_image(500, 685, image = img_bom2, tags = 'BOM')


# # Create a falling object (grasses)
grass1_id = canvas.create_image(1200, 565, image = img_grass1)
grass2_id = canvas.create_image(2385,565, image = img_grass2)
grass3_id = canvas.create_image(3400, 590, image = img_grass3)
grass6_id = canvas.create_image(400, 650, image = img_grass6)
grass6_id = canvas.create_image(1800, 650, image = img_grass6)
grass6_id = canvas.create_image(3200, 650, image = img_grass6)
grass7_id = canvas.create_image(1500, 700, image = img_grass7)
grass7_id = canvas.create_image(2600, 700, image = img_grass7)
grass7_id = canvas.create_image(3600, 700, image = img_grass7)

# # Create a falling object (stones)
stone3_id = canvas.create_image(1000, 685, image = img_stone3, tags= 'STONE')
stone2_id = canvas.create_image(2000, 685, image = img_stone2, tags= 'STONE')
stone3_id = canvas.create_image(2900, 685, image = img_stone3, tags= 'STONE')
stone1_id = canvas.create_image(200, 685, image = img_stone1, tags= 'STONE')

# # Create a falling object (dimond1)

dimond1_id = canvas.create_image(700, 690, image = img_dimond1)
dimond1_id = canvas.create_image(3000, 690, image = img_dimond1)
dimond1_id = canvas.create_image(1900, 690, image = img_dimond1)

# #.....Create a falling object (box)....

box1_id = canvas.create_image(595, 690, image = img_box1)
box1_id = canvas.create_image(650, 690, image = img_box1)
box1_id = canvas.create_image(650, 635, image = img_box1)

box1_id = canvas.create_image(1250, 690, image = img_box1)
box1_id = canvas.create_image(1300, 690, image = img_box1)
box1_id = canvas.create_image(1300, 635, image = img_box1)
box1_id = canvas.create_image(1350, 690, image = img_box1)
box1_id = canvas.create_image(1350, 635, image = img_box1)
box1_id = canvas.create_image(1350, 580, image = img_box1)

box1_id = canvas.create_image(2000, 690, image = img_box1)
box1_id = canvas.create_image(2080, 630, image = img_box1)
box1_id = canvas.create_image(2140, 630, image = img_box1)
box1_id = canvas.create_image(2200, 630, image = img_box1)
box1_id = canvas.create_image(2260, 630, image = img_box1)

box1_id = canvas.create_image(2800, 690, image = img_box1)
box1_id = canvas.create_image(3333, 690, image = img_box1)
box1_id = canvas.create_image(3460, 690, image = img_box1)


# ..................dimond​​ score.............

score_id = canvas.create_text(340, 50, text=" : 0 ", font=("bold", 20), fill="white")
dimond2_id = canvas.create_image(300, 50, image = img_dimond2)

## .................Level...............

score_id = canvas.create_text(150, 50, text="Level : 1 ", font=("bold", 20), fill="white")


# Function to update the object's position
xspeed=3
yspeed=3
def moveBom():
    global xspeed
    global yspeed
    canvas.move(bom_id, xspeed, yspeed)
    leftPos = canvas.coords(bom_id)
    topPos = canvas.coords(bom_id)
    rightPos = canvas.coords(bom_id)
    bottomPos = canvas.coords(bom_id)

    if rightPos[0] > SCREEN_WIDTH or leftPos[0] < 0:
        xspeed = -xspeed

    if bottomPos[1] > SCREEN_HEIGHT-200 or topPos[1] < 0  :
        yspeed = -yspeed
    canvas.after(10, moveBom)
canvas.after(10, moveBom)




#create player
X_VELOCITY = 9
Y_VELOCITY = 9


# player_img = Image.open('images/players/player_down.png')
# player_id = ImageTk.PhotoImage(player_img)
# player = canvas.create_image(150, 700, image=player_id )

# player_img2 =Image.open('images/players/player_left.png')
# player_id2 = ImageTk.PhotoImage(player_img2)

player1_img=Image.open('images/players/player1.png')
player1_id = ImageTk.PhotoImage(player1_img)
player1 = canvas.create_image(150, 653, image=player1_id )

player2_img =Image.open('images/players/player2.png')
player2_id = ImageTk.PhotoImage(player2_img)

#touch
def move_player1():
    coords= canvas.coords(player1)
    players1=canvas.find_withtag('STONE')
    overlap1= canvas.find_overlapping(coords[0], coords[1], coords[0]+player1_id.width(), coords[1]+player1_id.height())
    for py1 in players1:
        if py1 in overlap1:
            return py1
    return 0

# def move_player2():
#     coord= canvas.coords(actor_id)
#     players2=canvas.find_withtag('player2')
#     overlap2= canvas.find_overlapping(coord[0], coord[1], coord[0]+player_id.width(), coord[1]+player_id.height())
#     for player2 in players2:
#         if player2 in overlap2:
#             return player2
#     return 0

def game_lose():
    index =canvas.coords(player1)
    boms=canvas.find_withtag('BOM')
    over=canvas.find_overlapping(index[0], index[1], index[0]+img_bom.width(), index[1]+img_bom.height())
    for bom in boms:
        if bom in over:
            return True
    return False

# Window lose imge
game =Image.open('images/bg1.png')
lose = ImageTk.PhotoImage(game)
game_over =Image.open('images/game_over.png')
over = ImageTk.PhotoImage(game_over)

died =Image.open('images/died.png')
resize =died.resize((120,100))
player_died = ImageTk.PhotoImage(resize)

#Window lose
def lose_window():
    canvas.create_image(700,400, image=over, tags= 'LOSE')
    canvas.itemconfigure(player1, image =player_died)



def is_border_left():
        return canvas.coords(player1)[0] < 30

def is_border_right():
        return canvas.coords(player1)[0] > 4000

def is_border_top():
        return canvas.coords(player1)[1] < 30

def is_border_bottom():
        return canvas.coords(player1)[1] > 370

def move_shape(event):
    if event.keysym == "Left" and not is_border_left():
        canvas.move(player1, -10, 0)
        canvas.itemconfigure(player1, image = player2_id)
    elif event.keysym == "Right" and not is_border_right():
        canvas.move(player1, 10, 0)
        canvas.itemconfigure(player1, image = player1_id)
    elif event.keysym == "Up" and not is_border_top():
        canvas.move(player1, 0, -10)
    elif event.keysym == "Down" and not is_border_bottom():
        canvas.move(player1, 0, 10)

    if  game_lose():
        lose_window()

#Gravity

#No auto scroll
def scroll_right(event):
    canvas.xview('scroll', 1, 'units')
    move_shape(event)

def scroll_left(event):
    canvas.xview('scroll', -1, 'units')

window.bind("<Key>", move_shape)
# window.bind("<Right>", scroll_right)

window.mainloop()
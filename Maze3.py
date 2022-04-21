from tkinter import *
from wall import *
from Animation import *
from Boulder import *

class Maze3:
    
    def __init__(self):
        self.window = Tk()
        
        self.canvas = Canvas(self.window, bg="black", width=800, height=800)
        self.canvas.pack()
        
        a = "white"
        self.wall_list = []
        self.boulder_list = []
        self.blinking_wall_list = []
        
        #creates all the walls for the maze
        wall1 = Wall(self.canvas, 0, 0, 800, 10, a, a)
        self.wall_list.append(wall1)
        
        wall2 = Wall(self.canvas, 0, 79, 10, 721, a, a)
        self.wall_list.append(wall2)
        
        wall3 = Wall(self.canvas, 10, 790, 790, 10, a, a)
        self.wall_list.append(wall3)
        
        wall4 = Wall(self.canvas, 790, 10, 10, 711, a, a)
        self.wall_list.append(wall4)
        
        wall5 = Wall(self.canvas, 10, 79, 158, 10, a, a)
        self.wall_list.append(wall5)
        
        wall6 = Wall(self.canvas, 79, 89, 10, 79, a, a)
        self.wall_list.append(wall6)
        
        wall7 = Wall(self.canvas, 10, 711, 79, 10, a, a)
        self.wall_list.append(wall7)
        
        wall8 = Wall(self.canvas, 237, 10, 10, 158, a, a)
        self.wall_list.append(wall8)
        
        wall9 = Wall(self.canvas, 158, 158, 79, 10, a, a)
        self.wall_list.append(wall9)
        
        wall10 = Wall(self.canvas, 158, 168, 10, 69, a, a)
        self.wall_list.append(wall10)
        
        wall11 = Wall(self.canvas, 79, 237, 168, 10, a, a)
        self.wall_list.append(wall11)
        
        wall12 = Wall(self.canvas, 79, 247, 10, 395, a, a)
        self.wall_list.append(wall12)
        
        wall13 = Wall(self.canvas, 89, 632, 69, 10, a, a)
        self.wall_list.append(wall13)
        
        wall14 = Wall(self.canvas, 158, 553, 10, 168, a, a)
        self.wall_list.append(wall14)
        
        wall15 = Wall(self.canvas, 168, 711, 312, 10, a, a)
        self.wall_list.append(wall15)
        
        wall16 = Wall(self.canvas, 237, 632, 10, 79, a, a)
        self.wall_list.append(wall16)
        
        wall17 = Wall(self.canvas, 474, 563, 10, 158, a, a)
        self.wall_list.append(wall17)
        
        wall18 = Wall(self.canvas, 553, 632, 10, 168, a, a)
        self.wall_list.append(wall18)
        
        wall19 = Wall(self.canvas, 563, 632, 79, 10, a, a)
        self.wall_list.append(wall19)
        
        wall20 = Wall(self.canvas, 632, 553, 10, 79, a, a)
        self.wall_list.append(wall20)
        
        wall21 = Wall(self.canvas, 642, 553, 79, 10, a, a)
        self.wall_list.append(wall21)
        
        wall22 = Wall(self.canvas, 711, 563, 10, 79, a, a)
        self.wall_list.append(wall22)
        
        wall23 = Wall(self.canvas, 632, 711, 158, 10, a, a)
        self.wall_list.append(wall23)
        
        wall24 = Wall(self.canvas, 247, 79, 158, 10, a, a)
        self.wall_list.append(wall24)
        
        wall25 = Wall(self.canvas, 237, 247, 10, 158, a, a)
        self.wall_list.append(wall25)
        
        wall26 = Wall(self.canvas, 316, 158, 10, 484, a, a)
        self.wall_list.append(wall26)
        
        wall27 = Wall(self.canvas, 326, 632, 79, 10, a, a)
        self.wall_list.append(wall27)
        
        wall28 = Wall(self.canvas, 326, 158, 79, 10, a, a)
        self.wall_list.append(wall28)
        
        wall29 = Wall(self.canvas, 158, 316, 10, 168, a, a)
        self.wall_list.append(wall29)
        
        wall30 = Wall(self.canvas, 168, 474, 79, 10, a, a)
        self.wall_list.append(wall30)
        
        wall31 = Wall(self.canvas, 237, 484, 10, 79, a, a)
        self.wall_list.append(wall31)
        
        wall32 = Wall(self.canvas, 247, 553, 69, 10, a, a)
        self.wall_list.append(wall32)
        
        wall33 = Wall(self.canvas, 326, 395, 237, 10, a, a)
        self.wall_list.append(wall33)
        
        wall34 = Wall(self.canvas, 474, 405, 10, 79, a, a)
        self.wall_list.append(wall34)
        
        wall35 = Wall(self.canvas, 395, 474, 10, 79, a, a)
        self.wall_list.append(wall35)
        
        wall36 = Wall(self.canvas, 395, 553, 168, 10, a, a)
        self.wall_list.append(wall36)
        
        wall37 = Wall(self.canvas, 553, 474, 10, 79, a, a)
        self.wall_list.append(wall37)
        
        wall38 = Wall(self.canvas, 563, 474, 158, 10, a, a)
        self.wall_list.append(wall38)
        
        wall39 = Wall(self.canvas, 711, 395, 10, 79, a, a)
        self.wall_list.append(wall39)
        
        wall40 = Wall(self.canvas, 632, 79, 10, 326, a, a)
        self.wall_list.append(wall40)
        
        wall41 = Wall(self.canvas, 642, 395, 69, 10, a, a)
        self.wall_list.append(wall41)
        
        wall42 = Wall(self.canvas, 711, 158, 79, 10, a, a)
        self.wall_list.append(wall42)
        
        wall43 = Wall(self.canvas, 711, 316, 79, 10, a, a)
        self.wall_list.append(wall43)
        
        wall44 = Wall(self.canvas, 642, 237, 79, 10, a, a)
        self.wall_list.append(wall44)
        
        wall45 = Wall(self.canvas, 642, 79, 79, 10, a, a)
        self.wall_list.append(wall45)
        
        wall46 = Wall(self.canvas, 553, 10, 10, 79, a, a)
        self.wall_list.append(wall46)
        
        wall47 = Wall(self.canvas, 474, 79, 79, 10, a, a)
        self.wall_list.append(wall47)
        
        wall48 = Wall(self.canvas, 474, 89, 10, 158, a, a)
        self.wall_list.append(wall48)
        
        wall49 = Wall(self.canvas, 326, 237, 148, 10, a, a)
        self.wall_list.append(wall49)
        
        wall50 = Wall(self.canvas, 553, 158, 79, 10, a, a)
        self.wall_list.append(wall50)
        
        wall51 = Wall(self.canvas, 553, 168, 10, 158, a, a)
        self.wall_list.append(wall51)
        
        wall52 = Wall(self.canvas, 395, 316, 158, 10, a, a)
        self.wall_list.append(wall52)
        
        #creates the boulders
        boulder1 = Boulder(19.5, 98.5, 50, "green", 701.5, self.window, self.canvas)
        self.boulder_list.append(boulder1)
        
        boulder2 = Boulder(730.5, 335.5, 50, "green", 701.5, self.window, self.canvas)
        self.boulder_list.append(boulder2)
        
        #calls animation
        Animation(self.window, self.canvas, 24.5, 24.5, self.wall_list, self.blinking_wall_list, self.boulder_list)
        


import tkinter

class Paddle: #develops the paddle class
    def __init__(self, c): #creates a drawing that is the size of the paddle
        self.__canvas = c

        self.__left = 200
        self.__right = 300
        self.__top = 570
        self.__bottom = 590

        self.__drawing = self.__canvas.create_rectangle(self.__left, self.__top, self.__right,self.__bottom, fill = "black") #Creates the paddle

    def get_top(self): #for use in the mouse movement, gets the top side of the paddle
        return self.__top
    def get_bottom(self): #for use in the mouse movement, gets the bottom side of the paddle
        return self.__bottom
    def get_left(self): #for use in the mouse movement, gets the left side of the paddle
        return self.__left
    def get_right(self): #for us in the mouse movemnt, gets the right side of the paddle
        return self.__right

    def mouse_move(self,event): #function is passed into this that determines what the mouse is doing.
        x_change = event.x - self.__left #determines the distance of the mouse from the left and right, through the function passed into it
        self.__left += x_change #when mouse moves left, move left
        self.__right += x_change #when mouse moves right, move right
        self.__canvas.move(self.__drawing,x_change, 0) #glues the paddle to the bottom, and draws the object there


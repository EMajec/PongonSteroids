import tkinter

class Ball: #creates my ball class
    def __init__(self, c, l , r, t, b): #gives us the size of the ball
        self.__canvas = c

        self.__left = l
        self.__right = r
        self.__top = t
        self.__bottom = b
        self.__canvas = c


        self.__x_speed = 3 #these give us the speed and direction of the balls which will later derive acceleration
        self.__y_speed = 4
        self.__x_direction = -1
        self.__y_direction = 1




        self.__drawing = self.__canvas.create_oval(self.__left, self.__top,self.__right,self.__bottom, fill = "orange") #draws the ball

    def move(self): #gives the ball motion that is passed into the animate function in Pong

        x_change = self.__x_speed * self.__x_direction #this gives the object motion in a horizontal direction by setting its position to change constantly
        y_change = self.__y_speed * self.__y_direction #this gives the object motion in the vertical direction by setting its position to change constantly

        self.__left += x_change #when the ball is moving left, change the position of the ball to be left
        self.__right += x_change #when the ball is moving right change the position of the ball to be right
        self.__top += y_change #when teh ball is moving up change the position of the ball to be moving upwards
        self.__bottom += y_change #when teh ball ball is moving down change the position of the ball to be moving down

        if self.__top <=0: #creates a bounce off the top of the canvas
            self.__y_direction = 1 #redirects the ball down when it reaches the top
        if self.__bottom >= 600: #checks if the all hit the bottom
            self.__y_direction = 0 #stops the ball when it hits the bottom
            self.__x_direction = 0 #stops the ball when it hits the bottom
        if self.__left <= 0: #checks for the ball bouncing off the left
            self.__x_direction = 1 #moves the ball right when it hits the left wall
        if self.__right >= 600: #checks for the ball bouncing off the right
            self.__x_direction = -1 #moves the ball left when it hits the right wall

        self.__canvas.move(self.__drawing, x_change, y_change) #makes the ball move according to the above information

    def check_collision(self, other): #if ball hits the paddle this is its reaction
            spawn = 0 #is the neutral number of the score and collision count
            if (self.__bottom >= other.get_top()) and self.__left <= other.get_right() and self.__right >= other.get_left(): #if the ball hits the paddle it moves in the opposite direction
                self.__y_direction = -1 #send the ball back up when it impacts
                self.__x_speed += 1 #sends the ball to the horizontal directions faster
                self.__y_speed += 1 #sends the ball to the vertical directions faster

                if self.__x_speed == 13 and self.__y_speed == 14: #on 10 collisions slow the ball back down to orignal speed
                    self.__x_speed = 3 #sets ball's horizontal speed back to normal
                    self.__y_speed = 4#sets ball's vertical speed back to normal
                    spawn += 1 #increases the score of the game by 1
            if self.__bottom >= 600: #if the ball hits the bottom
                negative = -1 #return a -1 to be passed to the score
                return negative #return the score back


            return spawn #retun this number for score and other areas in paddle



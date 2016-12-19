# Ethan Turner
# December 8th 2016
# 15 out of 15 because I added a new feature into the game where every 10bounces a new ball spawns and the score tracks how many balls are in the arena as the score
# Description: This is a game of Pong where every 10 hits a new ball spawns. When all your balls hit the bottom the game ends, and you can play again! Must have paddle.py and ball.py to play!



import tkinter #imports the tkinter program
import ball #imports my ball program
import paddle #imports my paddle program


class Pong: #creates my game
    def __init__(self): #initializes the game
        self.main_window = tkinter.Tk() #creates the main window for the game
        self.main_window.title("Pong") #titels the window of the game
        self.__canvas = tkinter.Canvas(self.main_window, bg="papaya whip", width=600, height=600) #creates the canvas where the game is played
        self.__scoreframe = tkinter.Frame(self.main_window) #creates a frame at the bottom where the score will be


        self.__canvas.pack() #packs the canvas
        self.__scoreframe.pack(side="bottom") #packs the scoreboard to the bottom

        self.__paddle = paddle.Paddle(self.__canvas) #creates the paddle in the canvas from the paddle file

        self.__balllist =[ball.Ball(self.__canvas, 340, 380, 50, 90)] #creates a list of balls to spawn, and new balls in the canvas are added here
        self.__scoreNum = 0 #set the initial score of the game to 0




        self.main_window.bind('<Motion>', self.__paddle.mouse_move) #attaches the paddle to the mouse so that when I move the mouse the paddle moves too
        self.__score = tkinter.Label(self.__scoreframe, text='Score: ' + (str(self.__scoreNum))) #creates a label in the scoreboard to track the score
        self.__score.pack(side="left") #packs the score to be at the left.


        self.animate() #runs teh animate funciton on items above

        tkinter.mainloop() #loops the game

    def animate(self): #addds my animate functions to the Pong Class

        for item in self.__balllist: #loops into the ball list of balls as balls are added

            item.move() #calls my move class from ball program to every ball that is in my balllist
            item.check_collision(self.__paddle) #checks the collision of every ball with my paddle

            spawn = item.check_collision(self.__paddle) #checks if ball has bounced off the paddle 10 times and sets the score
            if spawn == 1: #spawn can only equal 1, 0, or -1, when it is 1 the score will increase and a new ball will spawn
                self.__scoreNum += 1 #this adds to my score variable
                self.__score.config(text='Score: ' + (str(self.__scoreNum))) #this sets the new score variable
                self.__balllist.append(ball.Ball(self.__canvas, 320, 360, 10, 50)) #this adds a new ball to the list and spawns a new ball

            if spawn == -1: #if the ball hits the bottom, it will stop moving and you will lose a point.
                self.__scoreNum -=1 #subtacts a point from your score
                self.__score.config(text='Score '+ str(self.__scoreNum)) #updates the scoreboard
                self.__balllist.remove(item) #removes the ball from the list so that it will stop moving
                if len(self.__balllist) == 0: #if all of the balls hit the bottom, your score will go to 0
                    self.game_over() #if your score is 0 then it will run the game over function


        self.main_window.after(20, self.animate)
    def game_over(self): #this function destroys the game and gives you the option to play again or quit playing
        self.main_window.destroy() #this will destroy your background game for you to start over
        self.main_window2 = tkinter.Tk() #this creates a new window where you can choose to start over or quit.
        self.main_window2.title("GameOver") #this titles the gameover window
        self.__gameover = tkinter.Frame(self.main_window2) #this creates a frame in the window for choosing between playing again or quitting
        self.__again = tkinter.Label(self.__gameover, text="Would you like to play again?") #this is just the question printed in the window
        self.__play = tkinter.Button(self.main_window2, text='Play Again!', command= self.again) #this button calls the again function which restarts your game
        self.__quit = tkinter.Button(self.main_window2, text='Quit!', command= self.end) #this function calls the end function which terminates the window



        self.__gameover.pack() #the functions below organize the screen appropriately
        self.__again.pack(side ='top')
        self.__play.pack(side = 'left')
        self.__quit.pack(side = "right")
    def end(self): #this is the end funciton which simply destroys your gameover screen
        self.main_window2.destroy() #destroys your game over screen
    def again(self): #this is the again function which restarts the game
        game = Pong() #this sets the class to a variable
        game #this calls the game
        self.main_window2.destroy() #this destroys the back window, but doesn't work beause the funciton before it is still running before it gets to this...



game = Pong() #starts the first game


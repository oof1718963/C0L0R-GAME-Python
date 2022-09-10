from tkinter import *
import random

root = Tk()
root.title("Color Randomizer Game")
root.geometry("800x600")
root.configure(bg="#ffd6ff")

color_label = Label(root,bg="#ffd6ff",font=("Inter",15))
color_label.place(relx=0.5,rely=0.5,anchor=CENTER)

score_label = Label(root,text="Score: 0",bg="#C8B6FF",font=("Inter",18))
score_label.place(relx=0.05,rely=0.1,anchor=W)

input_value = Entry(root,bg="#E7C6FF",font=("Inter"))
input_value.place(relx=0.5,rely=0.6,anchor=CENTER)

class game:
    def __init__(self):
        self.__score = 0
        
    def updateGame(self):
        self.color = ["red","purple","maroon","skyblue","black","white","lightgreen","teal"]
        self.text_color = ["Red","Purple","Maroon","Skyblue","Black","White","Lightgreen","Teal"]
        self.random_number_for_text = random.randint(0,7)
        self.random_number_for_color = random.randint(0,7)
        color_label["fg"] = self.color[self.random_number_for_color]
        color_label["text"] = self.text_color[self.random_number_for_text]
        
    def __updateScore(self,input_value):
        if (input_value == self.color[self.random_number_for_color]):
            print(self.color[self.random_number_for_color])
            self.__score = self.__score + random.randint(0,7)
            score_label["text"] = "Score: " + str(self.__score)
            
    def publicFunction(self,input_value):
        self.__updateScore(input_value)
        
gameObj = game()
def getInput():
    value = input_value.get()
    gameObj.publicFunction(value)
    gameObj.updateGame()
    input_value.delete(0,END)
    
start_button = Button(root,text="Start",bg="#B8C0FF",fg="Black",font=("Inter",15),command=gameObj.updateGame)
start_button.place(relx=0.4,rely=0.7,anchor=CENTER)


check_button = Button(root,text="Check",font=("Inter",15),bg="#BBD0FF",fg="Black",command=getInput)
check_button.place(relx=0.6,rely=0.7,anchor=CENTER)

root.mainloop()
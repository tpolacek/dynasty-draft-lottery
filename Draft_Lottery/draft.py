import team             #necessary imports
import lottery
from Tkinter import *
import tkMessageBox

#create teams for the lottery
lob = team.Team("Legion of Boom", "Phil", 5, 10, 0, 1821)
eg = team.Team("El Guapo", "Shelhamer", 7, 8, 0, 2015)
boobs = team.Team("boobs", "Grobe", 7,8, 0, 1892)
geag = team.Team("Green Eggs & Graham", "Tim", 8, 7, 0, 2024)
huw = team.Team("hide ur wife", "Jordan", 5, 10, 0, 1949)
ml = team.Team("Monkey Largo", "Brogan", 4, 11, 0, 1650)

#place teams in a list
teams = [lob, boobs, eg, geag, huw, ml]

#load the lottery object
lotto = lottery.Lottery(teams)

#create a standings in reverse order for the lottery object to use
standings = lotto.make_standings()

#set each teams winning combinations
lotto.set_team_combos()

#create a main GUI window
root = Tk()
root.wm_title("Dynasty Draft Lottery")

#create frames to hold interactive elements
rightFrame = Frame(root)
rightFrame.pack(side = RIGHT)

leftFrame = Frame(root)
leftFrame.pack(side = LEFT)

topFrame = Frame(root)
topFrame.pack(side = TOP)

bottomFrame = Frame(root)
bottomFrame.pack(side = BOTTOM)




#assign buttons, images, and what to display for each button when pressed

#Team 1
#show draft information function call for button
def show_team1():
    tkMessageBox.showinfo(teams[0].name + " Draft Information", teams[0].show_draft_info())

#create button for team 1
B1 = Button(topFrame, text = teams[0].name, command = show_team1)

#place image for team 1
C1 = Canvas(topFrame, height = 250, width = 300)
filename1 = PhotoImage(file = "bulls.gif")
image1 = C1.create_image(150, 150 , anchor = CENTER, image = filename1)
C1.pack(side = TOP)

#Team 2
def show_team2():
    tkMessageBox.showinfo(teams[1].name + " Draft Information", teams[1].show_draft_info())

B2 = Button(topFrame, text = teams[1].name, command = show_team2)

C2 = Canvas(topFrame, height = 250, width = 300)
filename2 = PhotoImage(file = "bears.gif")
image2 = C2.create_image(150, 150, anchor = CENTER, image = filename2)
C2.pack(side = BOTTOM)

#Team 3
def show_team3():
    tkMessageBox.showinfo(teams[2].name + " Draft Information", teams[2].show_draft_info())

B3 = Button(leftFrame, text = teams[2].name, command = show_team3)

C3 = Canvas(leftFrame, height = 250, width = 300)
filename3 = PhotoImage(file = "sox.gif")
image3 = C3.create_image(150, 150 , anchor = CENTER, image = filename3)
C3.pack(side = TOP)

#Team 4
def show_team4():
    tkMessageBox.showinfo(teams[3].name + " Draft Information", teams[3].show_draft_info())

B4 = Button(leftFrame, text = teams[3].name, command = show_team4)

C4 = Canvas(leftFrame, height = 250, width = 300)
filename4 = PhotoImage(file = "cubs.gif")
image4 = C4.create_image(150, 150 , anchor = CENTER, image = filename4)
C4.pack(side = BOTTOM)

#Team 5
def show_team5():
    tkMessageBox.showinfo(teams[4].name + " Draft Information", teams[4].show_draft_info())

B5 = Button(rightFrame, text = teams[4].name, command = show_team5)

C5 = Canvas(rightFrame, height = 250, width = 300)
filename5 = PhotoImage(file = "fire.gif")
image5 = C5.create_image(150, 150, anchor = CENTER, image = filename5)
C5.pack(side = TOP)

#Team 6
def show_team6():
    tkMessageBox.showinfo(teams[5].name + " Draft Information", teams[5].show_draft_info())

B6 = Button(rightFrame, text = teams[5].name, command = show_team6)

C6 = Canvas(rightFrame, height = 250, width = 300)
filename6 = PhotoImage(file = "hawks.gif")
image6 = C6.create_image(150, 150, anchor = CENTER, image = filename6)
C6.pack(side = BOTTOM)

#Run Lottery button and function call
def run_the_lotto():
    tkMessageBox.showinfo("Final Draft Lottery Results", lotto.run_lottery(standings))
    #end program and close window when user clicks OK
    root.destroy()

LottoButton = Button(bottomFrame, text = "Run Lottery", command = run_the_lotto)

#pack and run window
B1.pack(side = TOP)
B2.pack(side = BOTTOM)
B3.pack(side = TOP)
B4.pack(side = BOTTOM)
B5.pack(side = TOP)
B6.pack(side = BOTTOM)
LottoButton.pack(side = BOTTOM)

root.mainloop()

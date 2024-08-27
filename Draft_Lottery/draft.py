import team             #necessary imports
import lottery

import tkinter as tk
from tkinter import messagebox

#create teams for the lottery
fft  = team.Team("boobs"                    , "Grobe"   , 9, 6,     0, 1953)
sad  = team.Team("T-Mart"                   , "Martin"  , 6, 9,     0, 1676)
alb  = team.Team("ALL BALLS"                , "Brogan"  , 3, 12,    0, 1679)
elg  = team.Team("Aiyuken"                  , "Tunk"    , 8, 7,     0, 2126)
tmt  = team.Team("Switch All Day"           , "Andi"    , 3, 12,    0, 1603)
huw  = team.Team("Fantasy Football Team"    , "Phil"    , 7, 8,     0, 1840)

#place teams in a list
teams = [fft, sad, alb, elg, tmt, huw]

#load the lottery object
lotto = lottery.Lottery(teams)

#create a standings in reverse order for the lottery object to use
standings = lotto.make_standings()

#set each teams winning combinations
lotto.set_team_combos()

#create a main GUI window
root = tk.Tk()
root.wm_title("Dynasty Draft Lottery")

#create frames to hold interactive elements
rightFrame = tk.Frame()
rightFrame.pack(side = tk.RIGHT)

leftFrame = tk.Frame()
leftFrame.pack(side = tk.LEFT)

topFrame = tk.Frame()
topFrame.pack(side = tk.TOP)

bottomFrame = tk.Frame()
bottomFrame.pack(side = tk.BOTTOM)

#assign buttons, images, and what to display for each button when pressed

#Team 1
#show draft information function call for button
def show_team1():
    messagebox.showinfo(teams[0].name + " Draft Information", teams[0].show_draft_info())

#create button for team 1
B1 = tk.Button(topFrame, text = teams[0].name, command = show_team1)

#place image for team 1
C1 = tk.Canvas(topFrame, height = 250, width = 300)
filename1 = tk.PhotoImage(file = "bulls.gif")
image1 = C1.create_image(150, 150 , anchor = tk.CENTER, image = filename1)
C1.pack(side = tk.TOP)

#Team 2
def show_team2():
    messagebox.showinfo(teams[1].name + " Draft Information", teams[1].show_draft_info())

B2 = tk.Button(topFrame, text = teams[1].name, command = show_team2)

C2 = tk.Canvas(topFrame, height = 250, width = 300)
filename2 = tk.PhotoImage(file = "bears.gif")
image2 = C2.create_image(150, 150, anchor = tk.CENTER, image = filename2)
C2.pack(side = tk.BOTTOM)

#Team 3
def show_team3():
    messagebox.showinfo(teams[2].name + " Draft Information", teams[2].show_draft_info())

B3 = tk.Button(leftFrame, text = teams[2].name, command = show_team3)

C3 = tk.Canvas(leftFrame, height = 250, width = 300)
filename3 = tk.PhotoImage(file = "sox.gif")
image3 = C3.create_image(150, 150 , anchor = tk.CENTER, image = filename3)
C3.pack(side = tk.TOP)

#Team 4
def show_team4():
    messagebox.showinfo(teams[3].name + " Draft Information", teams[3].show_draft_info())

B4 = tk.Button(leftFrame, text = teams[3].name, command = show_team4)

C4 = tk.Canvas(leftFrame, height = 250, width = 300)
filename4 = tk.PhotoImage(file = "cubs.gif")
image4 = C4.create_image(150, 150 , anchor = tk.CENTER, image = filename4)
C4.pack(side = tk.BOTTOM)

#Team 5
def show_team5():
    messagebox.showinfo(teams[4].name + " Draft Information", teams[4].show_draft_info())

B5 = tk.Button(rightFrame, text = teams[4].name, command = show_team5)

C5 = tk.Canvas(rightFrame, height = 250, width = 300)
filename5 = tk.PhotoImage(file = "fire.gif")
image5 = C5.create_image(150, 150, anchor = tk.CENTER, image = filename5) 
C5.pack(side = tk.TOP)

#Team 6
def show_team6():
    messagebox.showinfo(teams[5].name + " Draft Information", teams[5].show_draft_info())

B6 = tk.Button(rightFrame, text = teams[5].name, command = show_team6)

C6 = tk.Canvas(rightFrame, height = 250, width = 300)
filename6 = tk.PhotoImage(file = "hawks.gif") 
image6 = C6.create_image(150, 150, anchor = tk.CENTER, image = filename6) # Here is the change to make 2 pictures the same
C6.pack(side = tk.BOTTOM)

#Run Lottery button and function call
def run_the_lotto():
    results = lotto.run_lottery(standings)
    messagebox.showinfo("Final Draft Lottery Results", results)

    # provide text output of each teams balls and the winning results
    with open('results.txt', 'w') as f:
        for t in teams:
            f.write(t.show_draft_info())
            f.write('\n')
        f.write(results)

    #end program and close window when user clicks OK
    root.destroy()

LottoButton = tk.Button(bottomFrame, text = "Run Lottery", command = run_the_lotto)

#pack and run window
B1.pack(side = tk.TOP)
B2.pack(side = tk.BOTTOM)
B3.pack(side = tk.TOP)
B4.pack(side = tk.BOTTOM)
B5.pack(side = tk.TOP)
B6.pack(side = tk.BOTTOM)
LottoButton.pack(side = tk.BOTTOM)

root.mainloop()

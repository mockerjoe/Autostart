import tkinter as tk
from tkinter import *
from tkinter import filedialog
import os

checkgame = os.path.exists("game.txt")
checkwork = os.path.exists("work.txt")

if checkgame == False:
	my_file = open("game.txt", "w+")
	print("Datei game.txt wurde erzeugt.")
else:
	print("Datei game.txt bereits vorhanden.")

if checkwork == False:
	my_file = open("work.txt", "w+")
	print("Datei work.txt wurde erzeugt.")
else:
	print("Datei work.txt bereits vorhanden.")

def browseFilesGame():
	filename = filedialog.askopenfilename(initialdir = "/",
										title = "Select a File",
										filetypes = (("Text files", "*.txt*"), ("all files", "*.*")))
	
	# Change label contents
	#label_file_explorer.configure(text="File Opened: " + filename)
	
	myText = open(r'game.txt','a')
	myString = filename
	myText.write("subprocess.Popen('" + myString + "')" + "\r\n")
	myText.close()
	
def browseFilesWork():
	filename = filedialog.askopenfilename(initialdir = "/",
										title = "Select a File",
										filetypes = (("Text files", "*.txt*"), ("all files", "*.*")))
	
	# Change label contents
	#label_file_explorer.configure(text="File Opened: " + filename)
	
	myText = open(r'work.txt','a')
	myString = filename
	myText.write("subprocess.Popen('" + myString + "')" + "\r\n")
	myText.close()
	
# Create the window
browser = Tk()

# Set window title
browser.title('skrr skrr engine v0.2')

# Set browser icon
#browser.tk.call("wm", "iconphoto", browser._w, tk.PhotoImage(file="icons/find.png"))

# Set window size
browser.geometry("530x200")
browser.resizable(False, False)

#Set window background color
browser.config(background = "white")

# Create a File Explorer label
label_file_explorer = Label(browser, text = "File Explorer auf Tkinter Basis",
								width = 75, height = 4, fg = "blue")

	
button_explore_game = Button(browser, text = "Browse Files for game",
							command = browseFilesGame)

button_explore_work = Button(browser, text = "Browse Files for work",
							command = browseFilesWork)

button_exit = Button(browser, text = "Exit",
						command = browser.destroy)

# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns
label_file_explorer.grid(column = 1, row = 1)

button_explore_game.grid(column = 1, row = 2)

button_explore_work.grid(column = 1, row = 3)

button_exit.grid(column = 1,row = 4)

# Let the window wait for any events
browser.mainloop()

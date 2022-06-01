import subprocess, webbrowser, os
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

checkgame = os.path.exists("game.txt")
checkwork = os.path.exists("work.txt")

# Function for Button
def game():

    if checkgame == False:                  #Check if file or path exists
        my_file = open("game.txt","w+")     #Create file if it doest exist
        print("Datei game.txt wurde erzeugt.")
    else:
        # Remove empty lines from text file
        with open("game.txt") as reader, open("game.txt", "r+") as writer:
            for line in reader:
                if line.strip():
                    writer.write(line)
                writer.truncate()

        # Remove blank file paths
        try:
            with open("game.txt", "r") as fr:
                lines = fr.readlines()

                with open("game.txt", "w") as fw:
                    for line in lines:

                        if line.strip("\n") != "subprocess.Popen('')":
                            fw.write(line)
            print("gelöscht!")
        except:
            print("Es wurde nichts entfernt.")

        with open("game.txt", "r") as work:
            for line in work:
                exec(line)      #Open file if it already exists
                
    root.destroy()

def work():

    if checkwork == False:                  #Check if file or path exists
        my_file = open("work.txt","w+")     #Create file if it doest exist
        print("Datei work.txt wurde erzeugt.")
    else:
        # Remove empty lines from text file
        with open("work.txt") as reader, open("work.txt", "r+") as writer:
            for line in reader:
                if line.strip():
                    writer.write(line)
                writer.truncate()

        # Remove blank file paths
        try:
            with open("work.txt", "r") as fr:
                lines = fr.readlines()

                with open("work.txt", "w") as fw:
                    for line in lines:

                        if line.strip("\n") != "subprocess.Popen('')":
                            fw.write(line)
            print("gelöscht!")
        except:
            print("Es wurde nichts entfernt.")

        with open("work.txt", "r") as work:
            for line in work:
                exec(line)      #Open file if it already exists

    root.destroy()

def browseFiles():
    exec(open("browser.py").read())

# Create Window
root = Tk()
root.title("GinGaXTREME_Setup  v0.3") # GinGaXTREME_Setup, SwaGGerAuto$tart, $ugerbahbii, PuchachiMunanyoo 
root.geometry("475x175")
root.resizable(False, False)


# Set Window background color
#root.config(background = "blue")

# Button for gaming
gameButton = ttk.Button(root, text="Gaming", command=game).place(x=50, y=125)

# Button for working
workButton = ttk.Button(root, text="Working", command=work).place(x=150, y=125)

# Button for default start
defButton = ttk.Button(root, text="Default", command=root.destroy).place(x=350, y=125)

# Button for 
editButton = ttk.Button(root, text="Edit", command=browseFiles).place(x=250, y=125)

# Label for Window
Label(root, text="Wähle dein Startprofil: \n1. Gaming \n2. Work \n3. Default", font=('Consolas 15')).pack()

# Timer to kill Programm after set amount of ms
root.after(20000, lambda: root.destroy())

# Set icon for window
root.tk.call("wm", "iconphoto", root._w, tk.PhotoImage(file="icons/startup.png"))

# Run window
root.mainloop()

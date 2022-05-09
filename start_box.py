import subprocess, webbrowser
from tkinter import *
from tkinter import ttk

def main():
    entry = input("Wähle dein Startprofil: \n1. Gaming \n2. Work \n3. Default")

    if int(entry) == 1:
        game()
    elif int(entry) == 2:
        work()

def game():
    subprocess.Popen('D:\\Emlulator\\DS4windows\\DS4Windows.exe') #DS4 controller support
    subprocess.Popen('D:\\Emlulator\\publish\\Ryujinx.exe') #Switch emulator

def work():
    subprocess.Popen('D:\\JetBrains\\IntelliJ IDEA 2021.2.3\\bin\\idea64.exe') #IntelliJ IDEA
    #subprocess.Popen('D:\\JetBrains\\IntelliJ IDEA 2021.2.3\\bin\\idea64.exe') #PyCharm
    subprocess.Popen('D:\\Sublime Text\\sublime_text.exe') #Sublime text
    #subprocess.Popen('C:\\Program Files\\Mozilla Firefox\\Firefox.exe') #Firefox
    #webbrowser.open_new_tab('https://studip.hochschule-trier.de', new=2, autoraise=True)

#Create Window
root = Tk()
root.title("SwaGGerAuto$tart")
root.geometry("375x175")

#Button for gaming
gameButton = ttk.Button(root, text="Gaming", command=game()).place(x=50, y=125)

#Button for working
workButton = ttk.Button(root, text="Working", command=work()).place(x=150, y=125)

#Button for default start
defButton = ttk.Button(root, text="Default", command=root.destroy).place(x=250, y=125)

Label(root, text="Wähle dein Startprofil: \n1. Gaming \n2. Work \n3. Default", font=('Consolas 15')).pack()

root.mainloop()
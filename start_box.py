import subprocess
import tkinter as tk

#Create Window
window = tk.Tk()
window.title("SwaGGerAuto$tart")
window.geometry("400x200")
window.mainloop()

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
    subprocess.Popen('C:\\Program Files\\Mozilla Firefox\\Firefox.exe') #Firefox

main()
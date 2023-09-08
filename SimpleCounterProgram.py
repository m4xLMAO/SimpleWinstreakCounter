print("Please Wait..." + "\n")
import tkinter as tk
print("- Loaded Tkiner..")
import time
print("- Loaded Time..")
from datetime import date
print("- Loaded Datetime..")
from tkinter import PhotoImage
print("- Loaded PhotoImage..")
import os
print("- Loaded os..")
from PIL import Image, ImageTk
print("- Loaded Images..")
print(" ")
import pygame
print(" ")
print("- Loaded Sounds..")
from colorama import init, Fore, Back, Style
print("- Loaded Colorama..")
print("! Finished!" + "\n")

init()

print(Fore.GREEN + "Press 'Ctrl + p' to add +1")
print(Fore.RED + "Press 'Ctrl + r' to make it 0" + "\n")
print(Fore.YELLOW + "Made By maxLMAO" + "\n")
print(Fore.LIGHTRED_EX + Back.GREEN + "// DO NOT CLOSE THIS WINDOW OR THE PROGRAM WILL CLOSE //")
print(Style.RESET_ALL)


class NumberGUI:
    def __init__(self):
        self.file_path2 = "Saves/date.txt"
        self.file_path = "Saves/number.txt"
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as f:
                lines = f.readlines()
                if len(lines) >= 3:
                    self.number = int(lines[0].strip())
                    self.numberws = int(lines[1].strip())
                    self.numberdw = int(lines[2].strip())
                else:
                    self.number = 0
                    self.numberws = 0
                    self.numberdw = 0
        else:
            self.number = 0
            self.numberws = 0
            self.numberdw = 0

                
        self.root = tk.Tk()        
        self.root.state("zoomed")

        self.root.configure(bg='gray')

        
        self.root.title("Simple Winstreak counter")

        def button_exit():
            self.root.destroy()
            
        self.bexit = tk.Button(self.root, text="Exit", command=button_exit)
        self.bexit.pack(side="top", anchor="ne", padx=10, pady=10)

        self.label = tk.Label(self.root, text="Winstreak: " + str(self.number), font=("Comic Sans MS", 32,'bold'),bg='gray',fg='white')
        self.label.pack(side="top", padx=10, pady=10)


        self.labelws = tk.Label(self.root, text="Daily Winstreak: " + str(self.numberws), font=("Comic Sans MS", 32,'bold'),bg='gray',fg='white')
        self.labelws.pack(side="top", padx=10, pady=10)

        self.labeldw = tk.Label(self.root, text="Daily Wins: " + str(self.numberdw), font=("Comic Sans MS", 32,'bold'),bg='gray',fg='white')
        self.labeldw.pack(side="top", padx=10, pady=10)

        

        self.label1 = tk.Label(self.root, text="Press 'Ctrl + p' to add +1\n Press 'Ctrl + r' to make it 0", font=("Comic Sans MS", 10),bg='gray',fg='white')
        self.label1.place(x=0,y=0)


        self.label2 = tk.Label(self.root, text="Made by maxLMAO! Discord: m4xLMAO", font=("Comic Sans MS", 10),bg='gray',fg='white')
        self.label2.pack(side="bottom", padx=10, pady=10)



        
        if os.path.exists(self.file_path2):
            with open(self.file_path2, "r") as f:
                rdate = f.readlines()

        if rdate:
            date_string = rdate[0]

            rdate = date_string.strip()  
            today = str(date.today())

            if today == rdate:
                self.labelws.configure(text="Daily Winstreak: " + str(self.numberws))
                self.labeldw.configure(text="Daily Wins: " + str(self.numberdw))
            
            else:

                self.numberws = 0
                self.numberdw = 0
                self.labeldw.configure(text="Daily Wins: " + str(self.numberdw))
                self.labelws.configure(text="Daily Winstreak: " + str(self.numberws))
        

        
        self.root.bind("<Key>", self.key_pressed)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        icon = tk.PhotoImage(file='static/Images/logo.png')
        self.root.iconphoto(True, icon)
        
        self.root.mainloop()

    def key_pressed(self, event):
        if event.keysym == "p" and event.state & 0x4:
            pygame.mixer.init()
            pygame.mixer.music.load("Static/Sounds/plus.mp3")
            pygame.mixer.music.play(loops=0)

            self.number += 1
            self.numberws += 1
            self.numberdw += 1

            self.label.configure(text="Winstreak: " + str(self.number))

            self.labelws.configure(text="Daily Winstreak: " + str(self.numberws))

            self.labeldw.configure(text="Daily Wins: " + str(self.numberdw))
            
        elif event.keysym == "r" and event.state & 0x4:
            pygame.mixer.init()
            pygame.mixer.music.load("Static/Sounds/reset.mp3")
            pygame.mixer.music.play(loops=0)

            self.number = 0
            self.numberws = 0


            self.label.configure(text="Winstreak: " + str(self.number))
            self.labelws.configure(text="Daily Winstreak: " + str(self.numberws))



        today = str(date.today())

        self.file_path2 = "Saves/date.txt"

        with open(self.file_path2, "w") as f:
            f.write(str(today) + "\n")


        with open(self.file_path, "w") as f:
            f.write(str(self.number) + "\n")
            f.write(str(self.numberws) + "\n")
            f.write(str(self.numberdw) + "\n")


    
    def on_closing(self):
        with open(self.file_path, "w") as f:
            f.write(str(self.number) + "\n")
            f.write(str(self.numberws) + "\n")
            f.write(str(self.numberdw) + "\n")

        self.root.destroy()

NumberGUI()

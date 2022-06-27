from tkinter import *
from tkinter import messagebox
import sys
import time
import threading
import random


class TypingSpeedTest:
    
    def __init__(self):
        self.window = Tk()
        self.window.title("Typing Speed Test")
        self.window.geometry("750x500")
        self.frame = Frame(self.window)
        
        self.sampleTexts = open("texts.txt", "r").read().split("\n")
        
        
        
        self.textLabel = Label(self.frame, text=random.choice(self.sampleTexts), font=("Helvetica", 18), wraplength=300, justify="center")
        self.textLabel.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        
        self.entryInput = Entry(self.frame, width=40, font=("Helvetica", 24))
        self.entryInput.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        self.entryInput.bind("<KeyPress>", self.start)
        
        self.speedLabel = Label(self.frame, text="Typing Speed: \n0.00 Characters per Second\n0.00 Characters per Minute", font=("Helvetica", 24))
        self.speedLabel.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
        
        self.resetButton = Button(self.frame, text="Reset", command=self.reset)
        self.resetButton.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        
        self.frame.pack(expand=True)
        
        self.counter = 0
        self.started = False
        
        self.window.mainloop()
        
    def start(self, event):
        if not self.started:
            if not event.keycode in [16, 17, 18]:
                self.started = True
                threadForTime = threading.Thread(target=self.timeThread)
                threadForTime.start()
        
        
        if not self.textLabel.cget('text').startswith(self.entryInput.get()):
            self.entryInput.config(fg="red")
        else:
            self.entryInput.config(fg="black")
        
        #need to exclude the last character
        if self.entryInput.get() == self.textLabel.cget('text'):
            self.started = False
            self.entryInput.config(fg="green")
            
        
    def timeThread(self):
        while self.started:
            time.sleep(0.1)
            self.counter += 0.1
            cps = len(self.entryInput.get()) / self.counter
            cpm = cps*60
            self.speedLabel.config(text=f"Typing Speed: \n{cps:.2f} Characters per Second\n{cpm:.2f} Characters per Minute")
        
    def reset(self):
        self.started = False
        self.counter = 0
        self.speedLabel.config(text="Typing Speed: \n0.00 Characters per Second\n0.00 Characters per Minute")
        self.textLabel.config(text=random.choice(self.sampleTexts))
        self.entryInput.delete(0, END)
    
    
    
TypingSpeedTest()






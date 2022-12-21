from tkinter import *
from tkinter import messagebox
import pyttsx3

def speak():
    t = entryText.get()
    engine.say(t)
    engine.runAndWait()
    engine.stop()
    
    if(t==''):
        messagebox.showinfo('Error', 'Enter text')

#starting pyttsx3
engine = pyttsx3.init()
win = Tk()
win.title('Reading Text')
win.configure(bg='silver')
win.geometry('510x120')

##label frame config
lf = LabelFrame(win, text='Write the text', font='35', bd='5')
lf.pack(fill='both', expand='yes', padx='12', pady='12')
Label(lf, text='Text', font='29', padx='14').pack(side='left')

###text input
text = StringVar()
entryText = Entry(lf, width=34, bd=5, font=20, textvariable=text)
entryText.pack(side='left', padx='11')

####Button
Button(lf, text='Speech', font=15, command=speak).pack(side='right')
mainloop()
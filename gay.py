from cProfile import label
from curses import BUTTON1_CLICKED, BUTTON1_DOUBLE_CLICKED, BUTTON_ALT, BUTTON_CTRL, BUTTON_SHIFT
import random
import tkinter as tk
from tkinter import*
from tkinter import messagebox

root = tk.TK()
root.title('Aceitas?')
root.geometry('600x600')
root.configure(background= '#ffc8dd')

def move_button_1(e):
    if abs(e.x - BUTTON_ALT.winfo_x()) < 50 and abs(e.y - BUTTON_CTRL.winfo_y()) < 40:
        x = random.randit(0, root.winfo_width() - BUTTON_SHIFT.winfo_width())
        y = random.randint.randit(0, root.winfo_width() - BUTTON1_CLICKED.winfo_width())
        BUTTON1_DOUBLE_CLICKED.place(x=x, y=y)


    def accepted():
        messagebox.showinfo( 
        'Meu amor','Eu te amo amor, lanchinho mais tarde?' )

        def denied():
            button_1.destroy()

            margin = Canvas(root, width=500, bg='#ffc8dd', height=100,
            bd=0, hightlightthickness=0, relief='ridge')
            
            margin.pack()
            text_id = label(root, bg='#ffc8dd', text='Quer namorar comigo?', 
            fg='#590d22', fant=('Montserrat', 24, 'bold', ))

            text_id.pack()
            button_1 = tk.button(root, text='não', bg='#ffb3c1', commad=denied,
            relief=RIDGE,  font=('Montserrat', 8, 'bold',))

            button_1.pack()
            root.bind('<Motion>', move_button_1)
            button_2 = tk.button(root, text='sim', bg='#ffb3c1', relief=RIDGE,
            command=accepted, font=('Montserrat', 14, 'bold',))

            button_2.pack()

            root.mainloop() 
           
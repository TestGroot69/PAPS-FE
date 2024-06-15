import tkinter
import random

root = tkinter.Tk()
root.geometry('540x540')
root.title('Roll Dice')

label = tkinter.Label(root, text='', font=('Arial Black', 260))


def roll_dice():
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    label.configure(text=f'{random.choice(dice)}')
    label.pack()


button = tkinter.Button(root, text='--- ROLL THE DICE ---', foreground='black', background="red", command=roll_dice, font=('Arial Black', 260))
button.configure(font=100)
button.pack()

root.mainloop()
from numpy import *
from tkinter import *
from tkinter import messagebox


# This function creates the die graphics
def TheDice():
    dienum = 0
    while dienum < die:
        current = result[dienum]
        #Very long die art
        dice_art =f"┌───────┐\n│       │\n│   {current}   │\n│       │\n└───────┘\n"
        dice_art2 = f"┌───────┐\n│       │\n│  {current}   │\n│       │\n└───────┘\n"
        dice_art3 = f"┌───────┐\n│       │\n│  {current}  │\n│       │\n└───────┘\n"
        txt_result.insert("end", f"Die # {dienum + 1}\n")
        if current > 99:
            txt_result.insert("end", dice_art3)
        elif current > 9:
            txt_result.insert("end", dice_art2)
        else:
            txt_result.insert("end", dice_art)
        dienum += 1


# This function generates the rules based the given specifications
def Roll():
    global result
    global side
    global die
    side = int(ent_side.get())
    die = int(ent_die.get())
    if side < 2 or side > 999 :
        messagebox.showerror("Information", f"Invalid ")
        return None
    txt_result['state'] = 'normal'
    txt_result.delete("1.0", "end")
    result = random.randint(1,side+1, size=die)
    TheDice()
    txt_result['state'] = 'disabled'

# Initialise the GUI
root = Tk()
root.title("Pocket Roller!")
root.geometry("300x650")
root.resizable(0, 0)
root.configure(bg='dodgerblue4')

# Entries for the sides and number of dice
ent_die = Entry(root,width=20)
ent_die.place(rely=0.08,relx=0.52)
ent_side = Entry(root,width=20)
ent_side.place(rely=0.23,relx=0.52)

# Button that executes the main function
btn_roll = Button(root, text= "Roll the dice!", command=lambda:Roll())
btn_roll.place(rely=0.28,relx=0.60)
btn_roll.configure(bg='#E3CF57')

# The Text area where  the dice are displayed
txt_result = Text(root, width=15, height=40)
txt_result.place(rely=0,relx=0.07)

# The Scrollbar for the results
sbar = Scrollbar(root, orient="vertical")
sbar.config(command=txt_result.yview)
txt_result.config(yscrollcommand = sbar.set)
sbar.pack(side="left", fill="y")
txt_result.configure(bg='#E3CF57')

lbl_die = Label(root, text = "How many dice do you\n want to roll?")
lbl_die.place(rely=0.02,relx=0.51)
lbl_die.configure(bg='dodgerblue4',foreground='white')
lbl_side = Label(root, text = "How many sides do you\n want your die to have? \n(Must be between 2 - 999)")
lbl_side.place(rely=0.15,relx=0.50)
lbl_side.configure(bg='dodgerblue4',foreground='white')

root.mainloop()

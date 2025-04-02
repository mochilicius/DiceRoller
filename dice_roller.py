import tkinter as tk
from tkinter import font
import random

root = tk.Tk()
root.title("Dice Roller")
root.geometry('400x250')

# base -------------------------------------------------------------------------------------------
root.configure(bg='#36393f')
mono_font = font.Font(family="Consolas", size=11)  # Monospace font for markdown style
bonus = 0

# result display frame ----------------------------------------------------------------------------
result_frame = tk.Frame(root, bg='#36393f')
result_frame.pack(pady=20, padx=20, anchor='w')

result_line1 = tk.Label(result_frame, text="1 #", bg='#36393f', fg='white', font=mono_font)
result_line2 = tk.Label(result_frame, text="2 Details: []", bg='#36393f', fg='#8e9297', font=mono_font)  # Darker gray
result_line1.pack(anchor='w')
result_line2.pack(anchor='w')

# frame for coin ----------------------------------------------------------------------------
top_button_frame = tk.Frame(root, bg='#36393f')
top_button_frame.pack(pady=(10, 5))

# coinflip! -----------------------------------------------------------------------------
coinflip_btn = tk.Button(top_button_frame, text="Coinflip", bg='#7289da', fg='white',
                         activebackground='#677bc4', relief='flat',
                         command=lambda: coinflip())
coinflip_btn.pack(side='left', padx=3)

# bonus ----------------------------------------------------------------------------
bonus_entry = tk.Entry(top_button_frame, width=6, font=mono_font, fg='#b9bbbe', relief='flat')
bonus_entry.insert(0, "Bonus")
bonus_entry.bind("<FocusIn>", lambda e: bonus_entry.delete(0, tk.END) if bonus_entry.get() == "Bonus" else None)
bonus_entry.bind("<FocusOut>", lambda e: bonus_entry.insert(0, "Bonus") if not bonus_entry.get() else None)
bonus_entry.pack(side='left', padx=3)  # Changed from grid to pack

# dices ----------------------------------------------------------------------------
button_frame = tk.Frame(root, bg='#36393f')
button_frame.pack(pady=5)

dice_buttons = [
    ("d4", 4), ("d6", 6), ("d8", 8), ("d10", 10),
    ("d12", 12), ("d20", 20), ("d100", 100)
]
for i, (text, sides) in enumerate(dice_buttons):
    btn = tk.Button(button_frame, text=text, bg='#7289da', fg='white',
                    activebackground='#677bc4', relief='flat',
                    command=lambda s=sides: roll_dice(s))
    btn.grid(row=0, column=i, padx=3)

# FUNCTIONS!! ---------------------------------------------------------------------------------
def roll_dice(dice_sides):
    global bonus
    dice_result = random.randint(1, dice_sides)
    # bonus display if applicable
    try:
        bonus = int(bonus_entry.get()) if bonus_entry.get() and bonus_entry.get() != "Bonus" else 0
    except ValueError:
        bonus = 0

    total_result = dice_result + bonus
    result_line1.config(text=f"1 # {total_result}")
    # if bonus exists :
    bonus_text = f" + {bonus}" if bonus else ""
    result_line2.config(text=f"2 Details: [d{dice_sides} ({dice_result}){bonus_text}]")

    if dice_result == dice_sides:
        result_line1.config(fg='#43b581')  # Green for critical
        result_line1.config(text=f"1 # {total_result} (CRITICAL!)")
    elif dice_result == 1:
        result_line1.config(fg='#f04747')  # Red for fail
        result_line1.config(text=f"1 # {total_result} (FAIL!)")
    else:
        result_line1.config(fg='white')

def coinflip():
    colors = ['#7289da', '#f04747']  # Blue, Red
    current_color = getattr(coinflip, 'color_index', 0)

    result = random.choice(["Heads", "Tails"])

    result_line1.config(text=f"1 # {result}", fg=colors[current_color])
    result_line2.config(text="2 Details: [coin flip]")
    coinflip.color_index = 1 - current_color

root.mainloop()
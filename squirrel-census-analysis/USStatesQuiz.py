## get input from user
# check if it is in the 50_states.csv file
# if there is a match, write the name on image file based on States' coordination

import tkinter as tk
import turtle
import pandas
import config

##Screen Turtle
screen = turtle.Screen()
screen.title("U.S. States Quiz")
image = "blank_states_img.gif"
REF_W, REF_H = config.REF_W, config.REF_H  # Bu görsel için tipik ölçü (Angela Yu dataset)
screen.setup(REF_W, REF_H)
screen.bgpic(image)

counter = 0
wrong_guess_count = 0
guessed = set()

#Writer Turtle
writer = turtle.Turtle(visible=False)
writer.penup()


#Tkinter labels and entry widget
window = tk.Tk()
window.title(f"{counter}/50 States found")

# Adjust size
window.geometry("270x90")
# set minimum window size value
window.minsize(config.TK_WIDTH, config.TK_HEIGHT)
# set maximum window size value
window.maxsize(config.TK_WIDTH, config.TK_HEIGHT)

guess_label = tk.Label(window, text="Guess: ")
guess_label.grid(row=config.GUESS_ROW, column=config.GUESS_COLUMN, padx=config.GUESS_PX, pady=config.GUESS_PY, sticky=config.GUESS_STICKY)

entry = tk.Entry(window)
entry.grid(row=config.ENTRY_ROW, column=config.ENTRY_COLUMN, padx=config.ENTRY_PX, pady=config.ENTRY_PY, sticky=config.ENTRY_STICKY)
entry.focus()

wrong_count_label = tk.Label(window, text=f"Wrong guess count: {wrong_guess_count}")
wrong_count_label.grid(row=config.WRONG_COUNT_ROW, column=config.WRONG_COUNT_COLUMN, columnspan=config.WRONG_COUNT_SPAN, padx=config.WRONG_COUNT_PX, sticky=config.WRONG_COUNT_STICKY)

#Load data from the csv file
data = pandas.read_csv("50_states.csv", sep=",", header=0)
data["state_norm"] = data["state"].str.strip().str.lower()

def check_state_csv(event=None):
    global counter, wrong_guess_count
    val = entry.get().strip().lower()
    entry.delete(0, tk.END)
    if not val:
        return

    row = data[data["state_norm"] == val]
    print(val)
    if row.empty:
        wrong_guess_count += 1
        wrong_count_label.config(text=f"Wrong guess count: {wrong_guess_count}")
        return

    else:
        state_name = row.iloc[0]["state"]
        # aynı eyaleti ikinci kez yazma
        if state_name in guessed:
            return

        coords = [int(row.iloc[0]["x"]), int(row.iloc[0]["y"])]
        writer.goto(coords[0], coords[1])
        writer.color("#FF0000")
        writer.write(row.iloc[0]["state"], align=config.WRITING_ALIGN, font=config.WRITING_FONT)
        counter += 1
        window.title(f"{counter}/50 States Found")

#Buttons
tk.Button(window, text="OK", command=check_state_csv).grid(row=config.OK_BTN_ROW, column=config.OK_BTN_COLUMN, padx=config.OK_BTN_PX, pady=config.OK_BTN_PY, sticky=config.OK_BTN_STICKY)
tk.Button(window, text="Cancel",command=window.quit).grid(row=config.CANCEL_BTN_ROW, column=config.CANCEL_BTN_COLUMN, padx=config.CANCEL_BTN_PX, pady=config.CANCEL_BTN_PY, sticky=config.CANCEL_BTN_STICKY)

# Enter tuşu ile gönder
window.bind("<Return>", check_state_csv)

window.mainloop()
screen.exitonclick()

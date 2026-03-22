import tkinter as tk
import tkinter.font as tkFont
from pathlib import Path
from tkinter import ttk

import pandas as pd
import random

LANGUAGE_NAME_FONT = {"family":"Ariel", "size":40}
WORD_FONT = {"family":"Ariel", "size":50}
TOP_FRAME_FONT = {"family": "Ariel", "size":15}
BACKGROUND_COLOR = "#B1DDC6"
CARD_FRONT_COLOR = "#EEEEEE"
CARD_BACK_COLOR = "#7EBDB6"
ASKED_LANGUAGE= "SPANISH"
ANSWER_LANGUAGE = "ENGLISH"
SECONDS=5

#Image Paths Base Directory
BASE_DIR = Path(__file__).resolve().parent
running = False
seconds_left = SECONDS
after_id = None
score=0
wrong_count=0
total_word_count=1000
is_front = True

# -----------------------------------------------------FUNCTIONS-----------------------------------------------------#
def reset_screen():
    global running
    running = False
    seconds_left = SECONDS

def wrong_answer():
    global wrong_count
    wrong_count += 1
  
    shuffle_cards()
    reset_screen()

def correct_answer():
    global score
    score += 1
    score_variable.set(score)
    progressbar["value"] = 0
    shuffle_cards()
    reset_screen()

def shuffle_cards():
    data = pd.read_csv(str(BASE_DIR / "data" / "clean_flashcards.csv"), sep=",", encoding="utf-8")
    df = pd.DataFrame(data)
    row = df.sample(1).iloc[0]  # artık bir Series
    asked_word_variable.set(row["English"])
    answered_word_variable.set(row["Spanish"])
    print(asked_word_variable.get())
    print(answered_word_variable.get())
    # Eğer ayrı bir label için English göstereceksen:print(asked_word_variable.get())

def cancel_timer():
    timer_variable.set("00:10")
    progressbar["value"] = 0
    global after_id
    if after_id is not None:
        root.after_cancel(after_id)
        after_id = None

def update_timer():
    global seconds_left, after_id, running
    # label & bar
    timer_variable.set(f"{seconds_left:02d}s")
    progressbar["maximum"] = SECONDS
    progressbar["value"] = SECONDS - seconds_left  # dolarak gitsin
    set_bar_color()

    if not running:
        return  # pause edilmişse burada dur
    if seconds_left > 0:
        seconds_left -= 1
        after_id = root.after(1000, update_timer)
    else:
        # süre bitti
        running = False
        start_button.config(state=tk.NORMAL)
        # burada “wrong” sayabilir veya otomatik sonraki karta geçebilirsin

def start():
    global running, seconds_left
    cancel_timer()
    running = True
    seconds_left = SECONDS
    progressbar["value"] = 0
    start_button.config(state=tk.DISABLED)
    shuffle_cards()
    update_timer()

def pause():
    global seconds_left, after_id
    after_id = root.after(1000, pause)
    pause_button.config(state=tk.DISABLED)
    seconds_left = SECONDS

def resume():
    global running
    if seconds_left > 0 and not running:
        running = True
        update_timer()

def set_bar_color():
    if seconds_left <= 3:
        s.configure("Striped.Horizontal.TProgressbar", background="red")
    else:
        s.configure("Striped.Horizontal.TProgressbar", background="green")

#-----------------------------------------------------UI SETTING-----------------------------------------------------#

root = tk.Tk()
root.geometry("800x700")
root.maxsize(800,800)
root.minsize(800,800)
root.resizable(False,False)
root.title("Language Flashcard")
root.configure(background=BACKGROUND_COLOR)
root.rowconfigure(0,weight=1)
root.columnconfigure(0,weight=1)

s = ttk.Style()
s.theme_use('clam')
s.configure("Striped.Horizontal.TProgressbar", foreground='green', background='green')

asked_language_variable = tk.StringVar(value="Spanish")
asked_word_variable = tk.StringVar(value="")
answered_language_variable = tk.StringVar(value="English")
answered_word_variable = tk.StringVar(value="")
score_variable = tk.IntVar(value=0)

#-----------------------------------------------------TOP FRAME-----------------------------------------------------#
#Create Start/Pause/Resume
top_label_frame = tk.Frame(root, width=800, height=70, highlightthickness=0, bg=BACKGROUND_COLOR)
top_frame_font = tkFont.Font(family=TOP_FRAME_FONT["family"], size=TOP_FRAME_FONT["size"], slant="roman")
top_label_frame.rowconfigure(1,weight=0)
top_label_frame.columnconfigure(0,weight=1)
top_label_frame.columnconfigure(1,weight=1)
top_label_frame.columnconfigure(2,weight=1)
top_label_frame.columnconfigure(3,weight=1)
top_label_frame.columnconfigure(4,weight=0)


start_button = tk.Button(top_label_frame, text="Start ▶️", font=top_frame_font, fg="black", bg=BACKGROUND_COLOR, width=10, pady=10, padx=10, command=start)
start_button.grid(row=0, column=0)

pause_button = tk.Button(top_label_frame, text="Pause ⏸️", font=top_frame_font, fg="black", bg=BACKGROUND_COLOR, width=10, pady=10, padx=10, command=pause)
pause_button.grid(row=0, column=1)

resume_button = tk.Button(top_label_frame, text="Resume ⏯️", font=top_frame_font, fg="black", bg=BACKGROUND_COLOR, width=10, pady=10, padx=10)
resume_button.grid(row=0, column=2)

#Create Score Label
score_label = tk.Label(top_label_frame, textvariable=f"Score {score_variable}/50 - 1 Strike 🔥", font=top_frame_font, fg="black", bg=BACKGROUND_COLOR)
score_label.grid(row=0, column=4, sticky="e")

#Create timer label on top of the root parent
timer_variable = tk.StringVar(value="00:10")
timer_label = tk.Label(top_label_frame, text="⏱️", textvariable=timer_variable, font=top_frame_font, fg="black", bg=BACKGROUND_COLOR)
timer_label.grid(row=1, column=4, sticky="e")

#Create progressbar and progressbar label
pg_label = tk.Label(top_label_frame, text="Progress 🚀", font=top_frame_font, fg="black", bg=BACKGROUND_COLOR, padx=10, pady=10)
pg_label.grid(row=1, column=0)
progressbar = ttk.Progressbar(top_label_frame, maximum=10, length=600, mode="determinate", style='Striped.Horizontal.TProgressbar')
progressbar.grid(row=1, column=1, columnspan=2, sticky="ew")


top_label_frame.grid(row=1, column=0, padx=10, pady=10)
# Frame'in verdiğin genişlik/yüksekliği koruması için:
#top_label_frame.grid_propagate(False)

#-----------------------------------------------------MIDDLE - CANVAS-----------------------------------------------------#

#Create Canvas for card photos and labels
canvas = tk.Canvas(root, width=654, height=374, background="white", highlightthickness=0)
canvas.grid(row=2, column=0)

# create_image for creating CARD IMAGE
#Card Front
CARD_FRONT = BASE_DIR / "images" / "card_front.png"
card_front_img = tk.PhotoImage(file=str(CARD_FRONT), width=654, height=374)
canvas.card_front_image = card_front_img
w,h = card_front_img.width(), card_front_img.height()
canvas.create_image(w//2, h//2, anchor="center", image=canvas.card_front_image)

#Card Back
CARD_BACK = Path(__file__).parent / "images" / "card_back.png"
card_back_img = tk.PhotoImage(file=str(CARD_BACK), width=654, height=374)
canvas.card_wrong_image = card_back_img
#canvas.create_image(w//2, h//2, anchor="center", image=canvas.card_front_image, highlightthickness=0)

# create create_window for creating LABELS in GRID
labels_frame = tk.Frame(canvas)
labels_frame.grid_columnconfigure(0, weight=1)

language_font = tkFont.Font(family=LANGUAGE_NAME_FONT["family"],size=LANGUAGE_NAME_FONT["size"], slant="italic")
language_label = tk.Label(labels_frame, textvariable=asked_language_variable, font=language_font, bg=CARD_FRONT_COLOR, fg="black")
language_label.grid(row=0, column=0, pady=(8,2))

word_font = tkFont.Font(family=WORD_FONT["family"],size=WORD_FONT["size"], weight="bold")
word_label = tk.Label(labels_frame, textvariable=asked_word_variable, font=word_font, bg=CARD_FRONT_COLOR, fg="black")
word_label.grid(row=1, column=0, pady=(2,8))

canvas.create_window(325, 187, window=labels_frame, anchor="center")  # x,y koordinatıyla konumlandır

# Frame'in verdiğin genişlik/yüksekliği koruması için:
labels_frame.grid_propagate(True)

#--------------------------------------------------BOTTOM FRAME--------------------------------------------------#

bottom_frame = tk.Frame(root, background=BACKGROUND_COLOR)
bottom_frame.grid(row=3, column=0, sticky=tk.NSEW)
bottom_frame.columnconfigure(0,weight=1)
bottom_frame.columnconfigure(1,weight=1)

#Correct Image Load to Button
CORRECT_BUTTON_IMG = BASE_DIR / "images" / "correct.png"
correct_img = tk.PhotoImage(file=str(CORRECT_BUTTON_IMG))
bottom_frame.correct_image = correct_img

#Wrong Image Load to Button
WRONG_BUTTON_IMG = Path(__file__).parent / "images" / "wrong.png"
wrong_img = tk.PhotoImage(file=str(WRONG_BUTTON_IMG))
bottom_frame.wrong_image = wrong_img

correct_button =tk.Button(bottom_frame, text="Correct", image=bottom_frame.correct_image, command=correct_answer, width=130, height=100, highlightthickness=0)
correct_button.grid(row=0, column=0, sticky=tk.SW, padx=70, pady=70)

wrong_button =tk.Button(bottom_frame,text="Wrong", image=bottom_frame.wrong_image, command=wrong_answer, width=120, height=90, highlightthickness=0)
wrong_button.grid(row=0, column=1, sticky=tk.SE, padx=70, pady=70)


# Frame'in verdiğin genişlik/yüksekliği koruması için:
bottom_frame.grid_propagate(True)



root.mainloop()
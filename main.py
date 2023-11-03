from tkinter import *
import pandas
import random

# Source of words. First 500.
# https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/Contemporary_fiction
# Translated the words in GoogleSheets with =GOOGLETRANSLATE(text,"en","ro")

BACKGROUND_COLOR = "#B1DDC6"

CURRENT_CARD = {}

data = pandas.read_csv("data/English_Words_1.csv")
TO_LEARN = data.to_dict(orient="records")  # "records" is to have an item-value pair for each word


def next_card():
    global CURRENT_CARD, FLIP_TIMER
    window.after_cancel(FLIP_TIMER)  # cancel the 3 seconds delay
    CURRENT_CARD = random.choice(TO_LEARN)
    current_word = CURRENT_CARD["English"]

    canvas.itemconfig(canvas_image, image=card_front_image)
    canvas.itemconfig(card_title, text="English", fill="black")
    canvas.itemconfig(card_word, text=current_word, fill="black")

    FLIP_TIMER = window.after(3000, func=flip_card)  # 3 seconds delay applied again in case the user presses a button


def flip_card():
    global CURRENT_CARD
    translated_word = CURRENT_CARD["Romanian"]

    canvas.itemconfig(canvas_image, image=card_back_image)
    canvas.itemconfig(card_title, text="Romanian", fill="white")
    canvas.itemconfig(card_word, text=translated_word, fill="white")


# ________ UI _________ #
# Window
window = Tk()
window.title("Test Your English App")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

FLIP_TIMER = window.after(3000, func=flip_card)  # 3 seconds delay

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_image)  # 263 = 1/2 of the image size
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "italic"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
wrong_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
know_button = Button(image=check_image, highlightthickness=0, command=next_card)
know_button.grid(row=1, column=1)

next_card()  # so that it shows a word instead of blank text

window.mainloop()

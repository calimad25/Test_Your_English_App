from tkinter import *
import pandas
import random

"""
An app for testing the knowledge of the user's English.
The program starts with a random first word from the list, and after a 3 seconds delay will automatically 
show the Romanian translation. After that, the program is waiting for the user to click one of the two buttons.

If the user did not know the word, should press the red button.
If the user knew the word, should press the green button, in which case the word will be removed from the list and
will not show up again.

Source of words.
https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/Contemporary_fiction
Translated the words in GoogleSheets with =GOOGLETRANSLATE(text,"en","ro")
"""


BACKGROUND_COLOR = "#B1DDC6"
CURRENT_CARD = {}
TO_LEARN = {}

# _____ Mechanics _____ #
words_to_learn = pandas.DataFrame()

try:  # When the program is run for the first time.
    data = pandas.read_csv("data/English_Words_1.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/English_Words_1.csv")
    TO_LEARN = original_data.to_dict(orient="records")  # "records" is to have an item-value pair for each word.
else:
    TO_LEARN = data.to_dict(orient="records")


def next_card():
    global CURRENT_CARD, FLIP_TIMER
    window.after_cancel(FLIP_TIMER)  # cancel the 3 seconds delay.
    CURRENT_CARD = random.choice(TO_LEARN)
    current_word = CURRENT_CARD["English"]

    canvas.itemconfig(canvas_image, image=card_front_image)
    canvas.itemconfig(card_title, text="English", fill="black")
    canvas.itemconfig(card_word, text=current_word, fill="black")

    FLIP_TIMER = window.after(3000, func=flip_card)  # 3 seconds delay applied again in case the user presses a button.


def flip_card():
    global CURRENT_CARD
    translated_word = CURRENT_CARD["Romanian"]

    canvas.itemconfig(canvas_image, image=card_back_image)
    canvas.itemconfig(card_title, text="Romanian", fill="white")
    canvas.itemconfig(card_word, text=translated_word, fill="white")


def knows_word():
    """Remove the known words and store the remaining ones in another csv that will be used next time."""
    TO_LEARN.remove(CURRENT_CARD)
    print(len(TO_LEARN))  # so user knows how many words there are left
    remaining_words = pandas.DataFrame(TO_LEARN)
    remaining_words.to_csv("data/words_to_learn.csv", index=False)  # so that it doesn't add double index nr in the csv.
    next_card()


# ________ UI _________ #
# Window
window = Tk()
window.title("Test Your English App")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

FLIP_TIMER = window.after(3000, func=flip_card)  # 3 seconds delay.

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_image)  # 263 = 1/2 of the image size.
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "italic"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
wrong_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
know_button = Button(image=check_image, highlightthickness=0, command=knows_word)
know_button.grid(row=1, column=1)

next_card()  # so that it shows a word instead of blank text.

window.mainloop()

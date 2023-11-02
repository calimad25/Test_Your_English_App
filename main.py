from tkinter import *
import pandas
import random

# Source of words. First 500.
# https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/Contemporary_fiction
# Translated the words in GoogleSheets with =GOOGLETRANSLATE(text,"en","ro")

BACKGROUND_COLOR = "#B1DDC6"

# ________ UI _________ #
# Window
window = Tk()
window.title("Test Your English App")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_image)  # 263 = 1/2 of the image size
card_title = canvas.create_text(400, 150, text="English", font=("Ariel", 40, "italic"))
cand_word = canvas.create_text(400, 263, text="Test", font=("Ariel", 60, "italic"))
canvas.grid(row=0, column=0, columnspan=2)

window.mainloop()

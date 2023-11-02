from tkinter import *
import pandas
import random

# https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/Contemporary_fiction
# The source of words. First 500.
# Translated the words in GoogleSheets with =GOOGLETRANSLATE(text,"ro","en")

BACKGROUND_COLOR = "#B1DDC6"

# ________ UI _________ #
# Window
window = Tk()
window.title("Test Your English App")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)


window.mainloop()

# importing modules
import tkinter
import os

# importing sub-modules
from tkinter import *
from gtts import gTTS
from datetime import datetime

# variable section
text = ""
file_name = datetime.now().strftime("text-to-audio-output-%Y%m%d%H%M%S")

# specific/thunder variable (metadata)
__version__ = "v1.0.0"
__updated__ = "04.12.2024"
__tag__ = "@dusanrsc"
__by__ = "Dusan Rosic"

# CONSTANTS section
TITLE = "Text-To-Audio Converter"

ROOT_WIDTH =  "600"
ROOT_HEIGHT = "415"
ROOT_SIZE = f"{ROOT_WIDTH}x{ROOT_HEIGHT}"

# hexadecimal color tuple CONSTANTS section
RED = "#FF0000"
GREEN = "#00FF00"
BLUE = "#0000FF"

ORANGE = "#FF6600"

BLACK = "#000000"
WHITE = "#FFFFFF"

ALPHA = GREEN

DEFAULT_COLOR = ORANGE

# program logic
def convert_text_to_audio():

	# gathering text from text input field
	text = text_input.get("1.0", tkinter.END)

	# convert the text to speech
	gtts = gTTS(text=text, lang="en")

	# save the audio file
	gtts.save(f"{file_name}.mp3")

	# play the converted audio
	os.system(f"start {file_name}.mp3")

# root window settings section
root = Tk()
root.title(f"{TITLE} | {__version__} | by: {__tag__}")
root.config(bg=WHITE)
root.geometry(ROOT_SIZE)
root.resizable(False, False)

# text input field
text_input = Text(root, fg=DEFAULT_COLOR)
text_input.pack()

# default text value in text input field
text_input.insert(tkinter.END, "Replace text here...")

# button for triggering program logic
convert_text_to_audio_button = Button(root, text="          Convert          ", font=("Arial Bold", 12), bg=DEFAULT_COLOR, fg=WHITE, relief=RIDGE, command=convert_text_to_audio)
convert_text_to_audio_button.pack(fill=BOTH)

# starting program (mainloop)
root.mainloop()
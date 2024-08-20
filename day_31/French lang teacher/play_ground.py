BACKGROUND_COLOR = "#B1DDC6"
from  random import randint

from tkinter import *
import pandas

def v_press():
    pass

def x_press():
    pass
#----------------------------------- sector to extract the data to csv --------------#
data_frame = pandas.read_csv("data/french_words.csv")  # import the data as a data frame

print(data_frame.French[randint(0, len(data_frame.French)-1)])

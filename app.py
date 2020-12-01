#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import time
import pickle as pkl
from datetime import datetime
from tkinter import *
from tkinter import messagebox
import collections 
#load last list of questions
with open('questions.pkl', 'rb') as f:
    last_questions = pkl.load(f)

url = "https://pt.stackoverflow.com/questions/tagged/python"

while True:
    response = requests.get(url)
    html=response.text.split("<div class=\"summary\">")

    current_questions=[]

    for i in range(1,16):
        current_questions.append(html[i].split(">")[1].split("/")[3].split("\"")[0].replace("%c3%a3","ã").replace("%c3%a7","ç")\
            .replace("%c3%a9","é").replace("%c3%b3","ó").replace("%c3%a1", "á"))

    # last_questions.sort()
    # current_questions.sort()

    if collections.Counter(last_questions) == collections.Counter(current_questions):
        print("No change", "\n\n")
    else:
        print("One new question at", datetime.now().strftime("%H:%M:%S"))
        print(current_questions[0])
        root = tkinter.Tk()
        root.geometry('+250+150')
        root.title('New questions')
        photo = tk.PhotoImage(file = "stack-overflow.png")
        root.iconphoto(False, photo)
        style = ThemedStyle(root)
        style.set_theme("arc")
        root.withdraw()

        # Message Box
        messagebox.showinfo("New Question SOpt", current_questions[0])
        with open('questions.pkl', 'wb') as f:
            pkl.dump(current_questions, f)

    time.sleep(600)
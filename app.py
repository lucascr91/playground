#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import time
import pickle as pkl
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
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

    last_questions.sort()
    current_questions.sort()

    if last_questions==current_questions:
        print("No change", "\n\n")
    else:
        print("Saving new list and sending you an email")
        print(datetime.now().strftime("%H:%M:%S"))
        with open('message.txt', 'rb') as fp:
            msg = MIMEText(fp.read())
        me = "lucas.cpp010@gmail.com"
        me_again = "lucas.cpp010@gmail.com"
        msg['Subject'] = 'New question python SOpt' % textfile
        msg['From'] = me
        msg['To'] = me_again
        # Send the message via our own SMTP server, but don't include the
        # envelope header.
        s = smtplib.SMTP('localhost')
        s.sendmail(me, [me_again], msg.as_string())
        s.quit()
        with open('questions.pkl', 'wb') as f:
            pkl.dump(current_questions, f)

    time.sleep(6000)
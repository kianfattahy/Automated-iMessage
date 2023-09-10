# -*- coding: utf-8 -*-
from file_processing import *
import os

with open('PhoneNumber.txt', 'r') as p:
    phone_number = p.read()

    
with open('text_to_send.txt', 'r') as t:
    text = t.read()
    
def send_messages(num, message):
    os.system('osascript sending_messages_copy.scpt {} "{}"'.format(num, message))

#extract sentences
sentence = get_sentences(text)

#send just the first sentence to phone number
send_messages(phone_number, sentence[0])

#now get rid of that line in the text file
data = text.splitlines(True)
with open('Desktop/pickup_line_sender/TEXT_TO_SEND_copy.txt', 'w') as fout:
    fout.writelines(data[1:])

t.close()
p.close()


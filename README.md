# iMessage Automation
This program allows the user to send automated iMessages to contacts, and it can be customized to send a message at determined intervals and/or send a mass number of messages that make up a text (like sending every line of Finding Nemo or your favorite song).

# Send Daily Messages
In order to send a message at pre-determined intervals, fill out the Text_to_send.txt file with your desired message. Then, simply setup a crontab file to execute messenger.py at the same time each day. As it stands, the program will delete the top line of a file every time it sends a message from it. 

For example, this format is good for sending a single joke per day that is selected from a text consisting of hundreds of jokes. However, the program can be customized to not edit the text file, in which case the user can send the same text every day.

# Send Multiple Messages at Once
Alternatively, the user can spam someone's phone by sending individual messages that make up every line of a larger text. 

For example, every line of your favorite movie can be sent to a friend, and the program will send every line back to back rapidly. This can result in thousands of messages being sent in a very short period of time.

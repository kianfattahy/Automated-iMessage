# iMessage Automation Tool

## Overview
This iMessage Automation Tool is designed to facilitate the automatic sending of iMessages from your device. Whether you want to send a daily joke to a friend, remind someone of a task at fixed intervals, or even flood their iMessages with lines from their favorite movie, this tool has you covered.

## Features

### Daily Automated Messages
- **Pre-set Intervals**: Configure the tool to send messages at specific times or intervals.
- **Dynamic Message Selection**: By default, the tool selects the top line from the `text_to_send.txt` file and sends it as a message. After sending, this line is removed, making it suitable for sending a new joke or message every day.
- **Static Message Option**: The tool can also be customized to send the same text every day without altering the `text_to_send.txt` file.

### Mass Messaging
- **Rapid Message Sending**: Send multiple messages back-to-back in quick succession.
- **Use Cases**: Ideal for sending every line of a song, movie, or any long text. Be cautious as this can send thousands of messages in a short span.

## Setup & Usage

### Preparation
1. Populate the `text_to_send.txt` file with the desired messages. Each line in the file will be treated as a separate message.

### Daily Automated Messages
1. Set up a crontab job (or similar scheduler) to execute `messenger.py` at your desired time.
2. If you want to send a different message each day, ensure that after each message is sent, the respective line in `text_to_send.txt` is deleted.

### Mass Messaging
1. Run `messenger.py`. Ensure that the `text_to_send.txt` file contains the lines of text you wish to send.
2. The program will rapidly send each sentence as a separate message.

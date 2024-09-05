# Verification notifications

The project is designed to receive notifications about work verification.

### How to install

Clone the repository

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:

```commandline
pip install -r requirements.txt
```

### Create a telegram bot

Create a telegram bot. He will send you notifications
about the verification of the work. Initialize communication with him.

### Environment variables

Save environment variables to a `.env` file

```commandline
TG_BOT_TOKEN=Telegram token of your bot 
DVMN_TOKEN=Your token on Devman
```
### Run

At startup, specify your chat id

```python
python main.py your_chat_id
```

### Project Goals

The code is written for educational purposes on online-course
for web-developers [dvmn.org](https://dvmn.org/).
import praw
import re
from config import config
from utils.telegram_utils import send_message

client_id = config["CLIENT_ID"]
client_secret = config["CLIENT_SECRET"]
username = config["USERNAME"]
password = config["PASSWORD"]
patterns = config["PATTERNS"]

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     password=password,
                     user_agent='RedditScout by /u/{username}',
                     username=username)

foundString = '''
----- ༼ つ ◕_◕ ༽つ     MATCHING SENTENCE FOUND    ༼ つ ◕_◕ ༽つ -----
'''

def send_alert(string):
	'''
	This is a placeholder for an alert mechanism, optimally Slack / Telegram 
	'''
	print(foundString)


def check_matches(string, regexs):
	alert = False
	for regexp in regexs:
		if regexp.search(string):
			alert = True
	if alert:
		send_alert(string)
		send_message(string)

def scan(subreddit):
	regexs = create_regexs()
	for comment in reddit.subreddit(subreddit).stream.comments():
	    print(comment.body)
	    check_matches(comment.body, regexs)


def create_regexs():
	regexs = []
	for pattern in patterns:
		regex = re.compile(pattern)
		regexs.append(regex)
	return regexs
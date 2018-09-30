from utils.reddit_actions import scan

def init():
	subreddit = input("Which subreddit do you want to scan?\n")
	print("Starting now!")
	scan(subreddit)

init()

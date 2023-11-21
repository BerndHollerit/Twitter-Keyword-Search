import tweepy

# Set up API credentials
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""

# Authenticate with Tweepy
auth = tweepy.OAuth1UserHandler(
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

api = tweepy.API(auth)

# Search Twitter for a keyword
keyword = 'DecisionCrew'
tweets = api.search_tweets(q=keyword, count=3)  # Adjust count as needed

# Write tweet text and author into a file
with open('tweets.txt', 'w', encoding='utf-8') as file:
    for tweet in tweets:
        file.write(f"{tweet.user.screen_name}: {tweet.text}\n")

print("Tweets saved to 'tweets.txt'.")

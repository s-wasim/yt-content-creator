import praw
import pandas as pd
from Secrets import REDDIT_SECRETS_STORE
from datetime import datetime

class RedditReader:
    def __init__(self):
        self.reddit = praw.Reddit(
            client_id=REDDIT_SECRETS_STORE['REDDIT_CLIENT_ID'],
            client_secret=REDDIT_SECRETS_STORE['REDDIT_CLIENT_SECRET'],
            user_agent=REDDIT_SECRETS_STORE['REDDIT_USER_AGENT']
        )
        self.submissions = []

    def read(self, subreddit='Python', limit=10, topic='hot'):
        match topic:
            case 'hot':
                submissions = self.reddit.subreddit(subreddit).hot(limit=limit)
            case 'new':
                submissions = self.reddit.subreddit(subreddit).new(limit=limit)
            case 'top':
                submissions = self.reddit.subreddit(subreddit).top(limit=limit)
            case 'random':
                self.reddit.subreddit(subreddit).random(limit=limit)
            case 'controversial':
                self.reddit.subreddit(subreddit).controversial(limit=limit)
            case 'rising':
                self.reddit.subreddit(subreddit).rising(limit=limit)
            case _:
                raise ValueError("Invalid topic. Choose from: (hot, new, top, random, rising, controversial)")
        self.submissions = [submission for submission in submissions]

    def __len__(self):
        return len(self.submissions)
    
    def __getitem__(self, ix):
        submission = self.submissions[ix]
        return {
            'title': submission.title,
            'score': submission.score,
            'id': submission.id,
            'url': submission.url,
            'created': datetime.fromtimestamp(submission.created).strftime('%d-%m-%Y %H:%M:%S'),
            'post': submission.selftext
        }
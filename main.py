from reddit_reader import RedditReader
from random import choice, randint

def create_yt_post_description(post):
    return f"Original post title:{post['title']} - {post['created']}\nLink to post: {post['url']}"

if __name__ == '__main__':
    topics = ['hot', 'new', 'top', 'random', 'rising', 'controversial']
    reader = RedditReader()
    reader.read(subreddit='AITAH', topic=choice(topics))
    sr_ix = randint(0, len(reader))
    print(create_yt_post_description(reader[sr_ix]), end='\n\n')
    print(f"{''.join(['-'] * 50)}POST{''.join(['-'] * 50)}", reader[sr_ix]['post'], sep='\n')
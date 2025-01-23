from reddit_reader import RedditReader
from random import choice, randint
from post_fix import fix_post

def create_yt_post_description(post):
    return f"Original post title:{post['title']} - {post['created']}\nLink to post: {post['url']}"

if __name__ == '__main__':
    # Read a random post from the subreddit AITAH
    topics = ['hot', 'new', 'top', 'rising']
    reader = RedditReader()
    reader.read(subreddit='AITAH', topic=choice(topics))
    sr_ix = randint(0, len(reader)) # Select a random post from the number of posts returned

    # Create youtube post description
    print(create_yt_post_description(reader[sr_ix]), end='\n\n')
    # Correct post text
    corrected_post = fix_post(reader[sr_ix]['post'])
    print(f"{''.join(['-'] * 50)}POST{''.join(['-'] * 50)}", *corrected_post, sep='\n')
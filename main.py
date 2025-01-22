from reddit_reader import RedditReader

if __name__ == '__main__':
    reader = RedditReader()
    reader.read()
    print('POST:', *reader[0].items(), 'wow', sep='\n\t')
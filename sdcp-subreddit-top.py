import praw
import csv

print('Subreddit Data Collection PRAW; by David E. Silva')

reddit = praw.Reddit(client_id = '', client_secret = '',
user_agent = 'loseitscript by /u/TechGeck', username = '', password = '')

subreddit = reddit.subreddit('Loseit')

with open('loseitdat.csv', 'w', newline = '', encoding = 'utf-8') as loseit:
    fieldnames = ['url', 'id', 'created', 'title', 'author', 'author_flair', 'text', 'score', 'ups', 'downs', 'comments']
    writer= csv.DictWriter(loseit, fieldnames = fieldnames)
    writer.writeheader()
    for submission in subreddit.top(limit=1000):
        writer.writerow({'url': submission.url, 'id': submission.id, 'created': submission.created, 'title': submission.title,
        'author': submission.author, 'author_flair': submission.author_flair_css_class, 'text': submission.selftext, 'score': submission.score,
        'ups': submission.ups, 'downs': submission.downs, 'comments': submission.num_comments})
        
print('Done')

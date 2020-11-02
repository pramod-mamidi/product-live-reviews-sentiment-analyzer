import praw
from textblob import TextBlob
import nltk
reddit = praw.Reddit(client_id='dwvhQN_PoUCoAw',
                     client_secret='X8N_SZUsiI-CNVIYLToBFFQ-cYE',
                     user_agent='news on hooks')
def text_blob_sentiment(review, sub_entries_textblob):
    analysis = TextBlob(review)
    if analysis.sentiment.polarity >= 0.0001:
        if analysis.sentiment.polarity > 0:
            sub_entries_textblob['positive'] = sub_entries_textblob['positive'] + 1
            return 'Positive'

    elif analysis.sentiment.polarity <= -0.0001:
        if analysis.sentiment.polarity <= 0:
            sub_entries_textblob['negative'] = sub_entries_textblob['negative'] + 1
            return 'Negative'
    else:
        sub_entries_textblob['neutral'] = sub_entries_textblob['neutral'] + 1
        return 'Neutral'
    # if analysis <0.43:
    #     sub_entries_textblob['negative'] = sub_entries_textblob['negative'] + 1
    #     return 'Negative'
    # elif analysis >0.57:
    #     sub_entries_textblob['positive'] = sub_entries_textblob['positive'] + 1
    #     return 'Positive'
    # else:
    #     sub_entries_textblob['neutral'] = sub_entries_textblob['neutral'] + 1
    #     return 'Neutral'
def replies_of(top_level_comment, count_comment, sub_entries_textblob):
    if len(top_level_comment.replies) == 0:
        count_comment = 0
        return
    else:
        for num, comment in enumerate(top_level_comment.replies):
            try:
                count_comment += 1
                text_blob_sentiment(comment.body, sub_entries_textblob)
            except:
                continue
            replies_of(comment, count_comment, sub_entries_textblob)


def main():
    p,n,ne=0,0,0
    l=[]
    for submission in top_posts:
        sub_entries_textblob = {'negative': 0, 'positive' : 0, 'neutral' : 0}
        print('Title of the post :', submission.title)
        text_blob_sentiment(submission.title, sub_entries_textblob)
        print("\n")
        submission_comm = reddit.submission(id=submission.id)

        for count, top_level_comment in enumerate(submission_comm.comments):
            count_comm = 0
            try :
                text_blob_sentiment(top_level_comment.body, sub_entries_textblob)
                replies_of(top_level_comment,
                           count_comm,
                           sub_entries_textblob)
            except:
                continue
        n+=int(sub_entries_textblob['negative'])
        p+=int(sub_entries_textblob['positive'])
        ne+=int(sub_entries_textblob['neutral'])
        print('Over all Sentiment of Topic by TextBlob :', sub_entries_textblob)
        print("\n\n\n")
    l.append(p)
    l.append(n)
    l.append(ne)
    return l

def call_reddit(n):
    global top_posts
    top_posts = reddit.subreddit(n).top('week', limit=40)
    lis=main()
    return(lis)

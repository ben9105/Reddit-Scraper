import praw
import pandas as pd
import datetime as dt
import credentials

# pull secret keys from seperate python script
reddit = praw.Reddit(client_id=credentials.client_id, \
                     client_secret=credentials.client_secret, \
                     user_agent=credentials.user_agent, \
                     user_name=credentials.user_name, \
                     password=credentials.password)

# search whichever subreddit you need
subreddit = reddit.subreddit("VinylDeals")

# top_subreddit = subreddit.top(limit=100)

# for submission in subreddit.top("day", limit=50):
#     print(submission.title, submission.url)

# return title and url from subreddit
topics_dict = {"title" : [], "url" : []}

# writing today's top 50 to index
for submission in subreddit.top("day", limit=50):
    topics_dict["title"].append(submission.title)
    topics_dict["url"].append(submission.url)

topics_data = pd.DataFrame(topics_dict)
#
# def get_date(created):
#     return dt.datetime.fromtimestamp(created)
#
# _timestamp = topics_data["created"].apply(get_date)
#
# topics_data = topics_data.assign(timestamp = _timestamp)

# output list to csv
topics_data.to_csv("Top_Albums.csv", index=False)

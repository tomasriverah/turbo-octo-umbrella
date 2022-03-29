
def most_retweeted(data):
    """
    Returns the top 10 tweets with the most retweets.
    """
    data.sort(key=lambda x: x['retweet_count'], reverse=True)
    return data[:10]

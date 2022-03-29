def most_active_users(data):
    """
    Returns a list of the 10 most active users in the given list of messages.
    """
    users = {}
    for tweet in data:
        if tweet.get('user', {}).get('id'):
            users[tweet['user']['id']] += 1
        else:
            users[tweet['user']['id']] = 1
    users = sorted(users.items(), key=lambda x: x[1], reverse=True)
    return users[:10]

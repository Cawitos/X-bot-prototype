import snscrape.modules.twitter as sntwitter
from models.comment import Comment


def get_replies(post_url, max_comments=1000):

    comments = []

    # Extraer ID del tweet
    tweet_id = post_url.split("/")[-1]

    query = f"conversation_id:{tweet_id}"

    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):

        if i >= max_comments:
            break

        comment = Comment(
            username=f"@{tweet.user.username}",
            text=tweet.content,
            date=tweet.date
        )

        comments.append(comment)

    return comments

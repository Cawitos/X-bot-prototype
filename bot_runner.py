from services.x_client import get_tweet_replies
from logic.answer_validator import is_valid_answer


def process_tweet(tweet_id, correct_answer):

    replies = get_tweet_replies(tweet_id)

    winners = []

    for reply in replies.get("data", []):
        
        comment = reply["text"]

        if is_valid_answer(comment, correct_answer):
            winners.append(reply["author_id"])

    return winners
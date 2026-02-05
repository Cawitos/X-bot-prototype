import re
from logic.normalizer import normalize
from logic.player_aliases import expand_aliases


def is_valid_answer(comment_text, correct_answer):

    normalized_comment = normalize(comment_text)
    allowed_answers = expand_aliases(correct_answer)

    tokens = re.findall(r'\b\w+\b', normalized_comment)

    for answer in allowed_answers:
        if answer in tokens:
            return True

    return False
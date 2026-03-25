import re
from logic.normalizer import normalize
from logic.player_aliases import expand_aliases


def is_valid_answer(comment_text, correct_answer):

    if not comment_text:
        return False

    normalized_comment = normalize(comment_text)
    allowed_answers = expand_aliases(correct_answer)

    numbers = re.findall(r'\d+', normalized_comment)

    tokens = re.findall(r'\b\w+\b', normalized_comment)

    for answer in allowed_answers:
        answer_str = str(answer).lower()

        if answer_str in tokens:
            return True

        if answer_str in numbers:
            return True

        if answer_str in normalized_comment:
            return True

    return False
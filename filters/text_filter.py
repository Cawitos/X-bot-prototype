from logic.validator import is_valid_answer


def filter_valid_comments(comments, correct_answer):

    return [
        c for c in comments
        if is_valid_answer(c.text, correct_answer)
    ]
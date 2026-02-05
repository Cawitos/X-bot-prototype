def match_exact(comment, targets):
    comment_clean = comment.strip().lower()

    for target in targets:
        if comment_clean == target.strip().lower():
            return True

    return False
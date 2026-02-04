def find_exact_matches(comments, target_text):

    matches = []

    for comment in comments:
        if comment.text.strip() == target_text.strip():
            matches.append(comment)

    return matches

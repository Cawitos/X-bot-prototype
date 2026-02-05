def first_participation_only(comments):

    seen = set()
    filtered = []

    for comment in comments:

        if comment.username not in seen:
            filtered.append(comment)
            seen.add(comment.username)

    return filtered
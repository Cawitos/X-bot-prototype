def select_winners(comments, winners_count):

    comments.sort(key=lambda x: x.created_at)

    return comments[:winners_count]
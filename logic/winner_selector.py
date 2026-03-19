import random


def select_winners(comments, winners_count):

    if not comments:
        return []

    # Si hay menos comentarios que ganadores pedidos
    if len(comments) <= winners_count:
        return comments

    # Seleccion aleatoria sin repetidos
    return random.sample(comments, winners_count)